#This is small task to send an E-mail using yagmail Library
import yagmail

receiver = "wojciechprimus@gmail.com"
body = "Hello there from Yagmail"
filename = "workingtime.txt"
passw = input('What is Yours Password:')

yag = yagmail.SMTP("wojciechprimus@gmail.com", passw)
yag.send(
    to=receiver,
    subject="Yagmail test with attachment",
    contents=body,
    attachments=filename,
)
