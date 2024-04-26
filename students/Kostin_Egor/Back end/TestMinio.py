from minio import Minio
import datetime
import io
from Outlook.outlook import Outlook
client = Minio(endpoint='localhost:9000',
                 access_key='minio',
                 secret_key='minio124',
                 secure=False)


mail = Outlook()
mail.login('suppnmzxis@outlook.com','1234Test')
mail.inbox()
mail.read()
attachments = mail.mailattachments()
client.make_bucket(bucket_name="name1") 
for filename, data in attachments:
            try:
                client.put_object(
                    "name1",
                    filename,
                    io.BytesIO(data),
                    len(data)
                )
            except Exception as err:
                print(err)
url = client.presigned_get_object(
            "name1",
            filename,
            expires=datetime.timedelta(hours=164)
        )
print(url)