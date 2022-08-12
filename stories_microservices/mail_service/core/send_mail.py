import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from core.config import EmailConfig


class SendMail(EmailConfig):
    def __init__(self, body, subject, subtype, recipients):
        self.body = body
        self.subject = subject
        self.subtype = subtype
        for recipient in recipients:
            message = self.prepare_message(recipient)
            self.send_mail(message, recipient)

    
    def prepare_message(self, recipient):
        message = MIMEMultipart("alternative")
        message["Subject"] = self.subject
        message["From"] = self.EMAIL_HOST_USER
        message["To"] = recipient
        part = MIMEText(self.body, self.subtype)
        message.attach(part)
        return message
        

    def send_mail(self, message, recipient):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(self.EMAIL_HOST_USER, self.EMAIL_HOST_PASSWORD)
            server.sendmail(
                self.EMAIL_HOST_USER, recipient, message.as_string()
            )
