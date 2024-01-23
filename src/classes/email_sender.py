import configparser
import smtplib
from email.message import EmailMessage

class EmailSender:

    def __init__(self, content):
        self.content = content
        self.subject = "WhatToWear Daily Recommendation"
        self.read_config()
        self.body = ""
        self.generate_body()

    def generate_body(self):
        if type(self.content) != list:
            print("Error: content is not a list")
            exit()

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
            print(f"Error: {e}")

    def read_config(self):
        config = configparser.ConfigParser()
        try:
            config.read('config/config.ini')

            self.user_email = config.get('EmailSender', 'user_email')
            self.password = config.get('EmailSender', 'password')

            self.host = config.get('EmailSender', 'host')
            self.port = int(config.get('EmailSender', 'port'))

            self.recipient_email = config.get('EmailSender', 'recipient_email')

        except AttributeError as e:
            print(f"Error reading config file: {e}")
            quit()
        
        except configparser.NoSectionError as e:
            print(f"Error reading config file: {e}")
            quit()
