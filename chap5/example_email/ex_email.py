import smtplib
from email.mime.text import MIMEText
import codecs

email_text = codecs.open('./textFile.txt', 'rb', 'utf-8')
msg = MIMEText(email_text.read())
email_text.close()

msg['Subject'] = 'Email example content'
msg['To'] = 'abmu333@hanmail.net'
msg['From'] = 'makingfunk@naver.com'

smtp_gmail = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtp_gmail.login(ID, passwd)
smtp_gmail.sendmail('', 'abmu333@hanmail.net', msg.as_string())
smtp_gmail.quit()
