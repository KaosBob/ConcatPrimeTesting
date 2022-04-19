import smtplib
import ssl
from email.mime.text import MIMEText


def sendEmail(receivers, subject="Subject not provided", body="Body not provided"):
    if subject == "":
        subject = "Subject not provided"
    if body == "":
        body = "Body not provided"

    sender = "ksb.pymail00@gmail.com"
    body = body + "<br><br><br><br><br>Sent by python"

    msg = MIMEText(body, "html")
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = ",".join(receivers)

    s = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    s.login("ksb.pymail00@gmail.com", "wzjhrjpsnnejmbrk")
    s.sendmail(sender, receivers, msg.as_string())
    s.quit()


if __name__ == "__main__":
    sendEmail(["ksb.test001@gmail.com"], "", "")
