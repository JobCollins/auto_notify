import smtplib
from email.message import EmailMessage


def email_alert(subject, body, address):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = address

    sender = "dulojob@gmail.com"
    msg['from'] = sender
    password = "mxuzftbmjmddyhxg"

    # set server params
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)
    server.send_message(msg)
    server.quit()


if __name__ == '__main__':
    email_alert("Automated Notification Test",
                "This is an automatic notification sent.", "dulo.collins@gmail.com")
