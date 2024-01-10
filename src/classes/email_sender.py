import configparser
import smtplib
from email.message import EmailMessage
import logging

'''
Reuseable class that sends emails, given a list of paragraphs as it's input.
Also needs a config.ini file for the user email and password, 
email services host adress (smtp.gmail.com for gmail) and port (587 for gmail), 
the recipients email, the subject for the email,and an optional intro message.
'''

class EmailSender:

    def __init__(self, content):
        self.content = content

        self.read_config()
        self.body = f"{self.intro}\n\n"
        self.generate_body()

    def generate_body(self):
        for i, paragraph in enumerate(self.content):
            if i != len(self.content) -1:
                self.body += f"{paragraph}\n\n"
            else:
                self.body += f"{paragraph}"

    def send_email(self):
        try:
            msg = EmailMessage()
            msg.set_content(self.body)

            msg["from"] = self.user_email
            msg["to"] = self.recipient_email
            msg["subject"] = self.subject

            with smtplib.SMTP(self.host, self.port) as server:
                server.starttls()
                server.login(self.user_email, self.password)
                server.send_message(msg)
        except Exception as e:
            logging.error(f"Error sending email: {e}")

    def read_config(self):
        config = configparser.ConfigParser()
        try:
            config.read('config/config.ini')

            self.user_email = config.get('WhatToWear', 'user_email')
            self.password = config.get('WhatToWear', 'password')

            self.host = config.get('WhatToWear', 'host')
            self.port = int(config.get('WhatToWear', 'port'))

            self.recipient_email = config.get('WhatToWear', 'recipient_email')
            self.intro = config.get('WhatToWear', 'intro')
            self.subject = config.get('WhatToWear', 'subject')
        except Exception as e:
            logging.error(f"Error reading configuration: {e}. make sure all fiels are filled in with no qutation marks")
