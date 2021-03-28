import os
import smtplib
from email.mime.text import MIMEText

from smtpapi import SMTPAPIHeader
from dotenv import load_dotenv
load_dotenv()


def main():
    server = create_smtp_server()

    from_email = os.environ['FROM_EMAIL']
    to_email = [
        os.environ['NOT_FOUND_EMAIL'],
        os.environ['EXISTS_EMAIL'],
    ]

    body = 'hello'
    message = MIMEText(body)
    message['From'] = from_email
    message['TO'] = ','.join(to_email)

    subject = 'メールバウンステスト'
    message['Subject'] = subject
    message['X-SMTPAPI'] = create_smtpapi_header(subject)

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


def create_smtpapi_header(subject):
    header = SMTPAPIHeader()
    header.set_unique_args({
        'foo': 'ふー',
        'subject': subject
    })
    return header.json_string()
    

if __name__ == '__main__':
    main()
