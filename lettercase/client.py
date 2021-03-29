import os
import smtplib
from email.mime.text import MIMEText

from smtpapi import SMTPAPIHeader
from dotenv import load_dotenv
load_dotenv()


def send(to_email):
    server = create_smtp_server()

    from_email = os.environ['FROM_EMAIL']
    to_email = [to_email]

    body = 'hello'
    message = MIMEText(body)
    message['From'] = from_email
    message['TO'] = ','.join(to_email)

    message['Subject'] = 'メールドロップテスト'

    server.sendmail(from_email, to_email, message.as_string())
    server.quit()


def create_smtp_server():
    host = 'smtp.sendgrid.net'
    port = 587
    user = 'apikey'
    password = os.environ['SENDGRID_API_KEY']
    server = smtplib.SMTP(host, port)
    server.starttls()
    server.login(user, password)
    return server


if __name__ == '__main__':
    main()
