import email
import email.header
import imaplib
import smtplib
import datetime
from email.mime.multipart import MIMEMultipart

from Outlook import config
import base64

class Outlook():
    def __init__(self):
        pass

    def login(self, username, password):
        self.username = username
        self.password = password
        login_attempts = 0
        while True:
            try:
                self.imap = imaplib.IMAP4_SSL(config.imap_server, config.imap_port)
                r, d = self.imap.login(username, password)
                assert r == 'OK', 'login failed: %s' % r
                print(" > Signed in as", self.username, d)
                return
            except Exception as err:
                print(" > Sign in error:", str(err))
                login_attempts += 1
                if login_attempts < 3:
                    continue
                assert False, 'login failed'

    def sendEmailMIME(self, recipient, subject, message):
        msg = MIMEMultipart()
        msg['to'] = recipient
        msg['from'] = self.username
        msg['subject'] = subject
        msg.add_header('reply-to', self.username)
        try:
            self.smtp = smtplib.SMTP(config.smtp_server, config.smtp_port)
            self.smtp.ehlo()
            self.smtp.starttls()
            self.smtp.login(self.username, self.password)
            self.smtp.sendmail(msg['from'], [msg['to']], msg.as_string())
            print("   email replied")
        except smtplib.SMTPException as e:
            print("Error: unable to send email", str(e))


    def sendEmail(self, recipient, subject, message):
        headers = "\r\n".join([
            "from: " + self.username,
            "subject: " + subject,
            "to: " + recipient,
            "mime-version: 1.0",
            "content-type: text/html"
        ])
        content = headers + "\r\n\r\n" + message
        attempts = 0
        while True:
            try:
                self.smtp = smtplib.SMTP(config.smtp_server, config.smtp_port)
                self.smtp.ehlo()
                self.smtp.starttls()
                self.smtp.login(self.username, self.password)
                self.smtp.sendmail(self.username, recipient, content.encode('utf-8'))
                print("   email sent.")
                return
            except Exception as err:
                print("   Sending email failed:", str(err))
                attempts += 1
                if attempts < 3:
                    continue
                raise Exception("Send failed. Check the recipient email address")
            
    def list(self):
        # self.login()
        return self.imap.list()

    def select(self, str):
        return self.imap.select(str)

    def inbox(self):
        return self.imap.select("Inbox")

    def junk(self):
        return self.imap.select("Junk")

    def logout(self):
        return self.imap.logout()

    def since_date(self, days):
        mydate = datetime.datetime.now() - datetime.timedelta(days=days)
        return mydate.strftime("%d-%b-%Y")

    def allIdsSince(self, days):
        r, d = self.imap.search(None, '(SINCE "'+self.since_date(days)+'")', 'ALL')
        list = d[0].decode('utf-8').split(' ')
        return list

    def allIdsToday(self):
        return self.allIdsSince(1)

    def readIdsSince(self, days):
        r, d = self.imap.search(None, '(SINCE "'+self.date_since(days)+'")', 'SEEN')
        list = d[0].decode('utf-8').split(' ')
        return list

    def readIdsToday(self):
        return self.readIdsSince(1)

    def unreadIdsSince(self, days):
        r, d = self.imap.search(None, '(SINCE "'+self.since_date(days)+'")', 'UNSEEN')
        list = d[0].decode('utf-8').split(' ')
        return list

    def unreadIdsToday(self):
        return self.unreadIdsSince(1)

    def allIds(self):
        r, d = self.imap.search(None, "ALL")
        list = d[0].decode('utf-8').split(' ')
        return list

    def readIds(self):
        r, d = self.imap.search(None, "SEEN")
        list = d[0].decode('utf-8').split(' ')
        return list

    def unreadIds(self):
        r, d = self.imap.search(None, "UNSEEN")
        print(d)
        list = d[0].decode('utf-8').split(' ')
        return list

    def hasUnread(self):
        list = self.unreadIds()
        return list != ['']

    def getIdswithWord(self, ids, word):
        stack = []
        for id in ids:
            self.getEmail(id)
            if word in self.mailbody().lower():
                stack.append(id)
        return stack

    def getEmail(self, id):
        r, d = self.imap.fetch(id, "(RFC822)")
        self.raw_email = d[0][1]
        self.email_message = email.message_from_bytes(self.raw_email)
        return self.email_message

    def unread(self):
        list = self.unreadIds()
        latest_id = list[-1]
        return self.getEmail(latest_id)

    def read(self):
        list = self.readIds()
        latest_id = list[-1]
        return self.getEmail(latest_id)

    def readToday(self):
        list = self.readIdsToday()
        latest_id = list[-1]
        return self.getEmail(latest_id)

    def unreadToday(self):
        list = self.unreadIdsToday()
        latest_id = list[-1]
        return self.getEmail(latest_id)

    def readOnly(self, folder):
        return self.imap.select(folder, readonly=True)

    def writeEnable(self, folder):
        return self.imap.select(folder, readonly=False)

    def rawRead(self):
        list = self.readIds()
        latest_id = list[-1]
        r, d = self.imap.fetch(latest_id, "(RFC822)")
        self.raw_email = d[0][1]
        return self.raw_email

    def mailbody(self):
        body = ""
        if self.email_message.is_multipart():
            for part in self.email_message.walk():
                # Пропускаем вложения
                if part.get_content_maintype() == 'multipart' or part.get('Content-Disposition') is not None:
                    continue
                # Получаем текстовую часть и добавляем её к переменной body
                if part.get_content_type() == 'text/plain':
                    body += part.get_payload(decode=True).decode('utf-8')
        else:
            # Если сообщение не является multipart, предполагаем, что оно содержит только текст
            body = self.email_message.get_payload(decode=True).decode('utf-8')
        return body

    def mailsubject(self):
        encoded_subject = self.email_message['Subject']

        # Проверка наличия кодирования
        if encoded_subject.startswith('=?UTF-8?B?'):
            # Удаление префикса и суффикса, оставляя только закодированную строку
            encoded_subject = encoded_subject[10:-1]

            # Декодирование строки из base64
            decoded_subject = base64.b64decode(encoded_subject).decode('utf-8')

            return decoded_subject
        else:
            # Если тема письма не была закодирована, возвращаем ее как есть
            return encoded_subject
    
    # def mailattachments(self):
    #     attachments = []

    #     for part in self.email_message.walk():
    #         if part.get_content_maintype() == 'multipart':
    #             continue
    #         if part.get('Content-Disposition') is None:
    #             continue
            
    #         # Получаем имя файла из заголовка Content-Disposition
    #         filename = part.get_filename()
    #         if filename:
    #             # Сохраняем вложение с оригинальным именем файла
    #             attachment_data = part.get_payload(decode=True)
    #             attachments.append((filename, attachment_data))
    #     return attachments
    def mailattachments(self):
        attachments = []

        for part in self.email_message.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            
            # Получаем имя файла из заголовка Content-Disposition
            filename_header = part.get_filename()
            if filename_header:
                filename = email.header.decode_header(filename_header)[0][0]
                # Если название файла закодировано в Base64, раскодируем его
                if filename_header.startswith('=?UTF-8?B?'):
                    encoded_text = filename_header.split('?')[-2]  # Getting the encoded text
                    filename = base64.b64decode(encoded_text).decode('utf-8')
                # Сохраняем вложение с оригинальным именем файла
                attachment_data = part.get_payload(decode=True)
                attachments.append((filename, attachment_data))
        return attachments
    
  
    def mailfrom(self):
        return self.email_message['from']

    def mailto(self):
        return self.email_message['to']

    def maildate(self):
        return self.email_message['date']

    def mailreturnpath(self):
        return self.email_message['Return-Path']

    def mailreplyto(self):
        return self.email_message['Reply-To']

    def mailall(self):
        return self.email_message

    def mailbodydecoded(self):
        return base64.urlsafe_b64decode(self.mailbody()).decode('utf-8')