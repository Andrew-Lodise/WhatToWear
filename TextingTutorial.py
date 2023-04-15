import smtplib
from email.message import EmailMessage


def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg["subject"] = subject
    msg["to"] = to

    user = "andrew8lodise@gmail.com"
    msg["from"] = user
    password = "qnotasugnwuhaowp"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()


email_message = "\nToday will be 80F. \nWear a short sleave shirt and shorts."
email_alert("WhatToWear Daily Recommendation", email_message, "lodise8@aol.com")
# if I want to go back to texting 6104570509@txt.att.net
