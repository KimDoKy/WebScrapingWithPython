import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

id = "id"
passwd = "passwd"

msg = MIMEText("The body of the email is here")
bsObj = BeautifulSoup(urlopen("http://isitchristmas.com/"),"lxml")

def sendMail(subject, body):
    global msg
    global bsObj
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "makingfunk0@gmail.com"
    msg['To'] = "abmu333@hanmail.net"
    while(bsObj.find("noscript").text == "아니요"):
        print("It is not Christmas yet.")
        time.sleep(3600)
        bsObj = BeautifulSoup(urlopen("https://isitchristmas.com"), "lxml")

sendMail("It's Christmas!", "According to http://isitchristmas.com, it is Christmas!")

s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
s.login(id, passwd)
s.sendmail("","abmu333@hanmail.net",msg.as_string())
# s.send_massege(msg)
s.quit()
