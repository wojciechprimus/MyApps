import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "wojciechprimus@gmail.com"
receiver_email = "wojciechprimus@gmail.com"
password = input("Type your password and press enter:")
message = """\
Subject: Hi My name is Python
I am writing now a message to You """

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
