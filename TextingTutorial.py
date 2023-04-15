import smtplib
from email.message import EmailMessage


def email_alert(body):
    msg = EmailMessage()
    msg.set_content(body)
    msg["subject"] = "WhatToWear Daily Recommendation"
    msg["to"] = "lodise8@aol.com"

    user = "andrew8lodise@gmail.com"
    msg["from"] = user
    password = "qnotasugnwuhaowp"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()


email_subject = "WhatToWear Daily Recommendation"
email_message = "\nToday will be 80F. \nWear a short sleave shirt and shorts."
target_email = "lodise8@aol.com"
target_text_email = "6104570509@txt.att.net"
# email_alert(email_subject, email_message, target_email)

# if I want to go back to texting 6104570509@txt.att.net
