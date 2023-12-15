import smtplib
from email.message import EmailMessage

# this currently always sends it to my aol email from my gmail email
class EmailMessenger:
    @staticmethod
    def send_email(body):
        msg = EmailMessage()
        msg.set_content(body)
        msg["subject"] = "WhatToWear Daily Recommendation"
        msg["to"] = "lodise8@aol.com"
        # target_text_email = "6104570509@txt.att.net" *if you want a text instead*

        user = "andrew8lodise@gmail.com"
        msg["from"] = user
        password = "qnotasugnwuhaowp"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user, password)
        server.send_message(msg)

        server.quit()
