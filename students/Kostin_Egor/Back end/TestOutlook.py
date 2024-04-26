from Outlook.outlook import Outlook
import os
from email.header import decode_header
import email.utils
# from models.models import Application
mail = Outlook()
mail.login('suppnmzxis@outlook.com','1234Test')
mail.inbox()
mail.read()
sus=mail.mailfrom()
# print(sus)
# bus=email.utils.parseaddr(sus)[0]
# print(bus)
print(f"Sdasdasd\nasdasd\n")
mail.sendEmail("pendospoganiy@gmail.com","sad","фывфыв\r\n\r\nфвыфывфыв\r\n\r\nывфвфвыфы\n\n")
# print(mail.mailattachments())
# def ANUS():
#     Apola = Application.add_application(1,mail.mailsubject(), mail.mailbody(), "sadad", 1, 1 )
# Сохраните каждое вложение в файл
# def decode_filename(filename):
#     decoded_header = decode_header(filename)
#     result = []
#     for part, encoding in decoded_header:
#         if isinstance(part, bytes):
#             result.append(part.decode(encoding or 'utf-8'))
#         else:
#             result.append(part)
#     return ''.join(result)
# def save_attachment(filename, data):
#     filename = decode_filename(filename)
#     with open(os.path.join('d:\\mail', filename), 'wb') as f:
#         f.write(data)
# for filename, attachment_data in attachments:
#     save_attachment(filename, attachment_data)