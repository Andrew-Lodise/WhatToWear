import configparser
import smtplib


from email.message import EmailMessage
from weatherman import Weatherman
from clothing_recommender import ClothingRecommender
# sends email to target email (from config.ini) from my gmail email
class EmailMessenger:

    def __init__(self, weatherman: Weatherman, clothing_recommender: ClothingRecommender):
        self.weatherman = weatherman
        self.body = f"Greetings from your What to Wear python project.\n"
        self.weather_output = weatherman.output
        self.recommendation = clothing_recommender.recommendation
        self.read_config()
        self.format_email()
    
    
    def send_email(self):
        msg = EmailMessage()
        msg.set_content(self.body)
        msg["subject"] = "WhatToWear Daily Recommendation"
        msg["to"] = self.email
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
        self.body += f"data retrieval method: {self.weatherman.method}\n\n"
        self.body += f"{self.weather_output}\n\n"
        self.body += f"{self.recommendation}"

    def read_config(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        self.email = config.get('WhatToWear', 'email')