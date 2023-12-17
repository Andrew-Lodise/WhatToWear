import smtplib
from email.message import EmailMessage

# this currently always sends it to my aol email from my gmail email
class EmailMessenger:

    def __init__(self, weather_output, recommendation):
        self.body = ""
        self.weather_output = weather_output
        self.recommedation = recommendation
        self.format_email()
    
    
    def send_email(self):
        msg = EmailMessage()
        msg.set_content(self.body)
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

    def print_email(self):
        print(self.body)

    
    def format_email(self):
        self.body += f"Greetings from your What to Wear python project.\n{self.weather_output}\n{self.recommedation}"