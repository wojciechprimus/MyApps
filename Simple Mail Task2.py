#This is small task to send an E-mail using smtplib Library

import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
passw = input('What is Yours Password:')


server.login("wojciechprimus",passw)
server.sendmail(
  "wojciechprimus@gmail.com",
  "wojciechprimus@gmail.com",
  "this message is from Simple Mail Task2 APP")
server.quit()
