import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '
family = 'abmu333@hanmail.net','makingfunk0@gmail.com'

msg = MIMEMultipart()
msg['Subject'] = 'image send mail test 2'

msg['From'] = 'makingfunk0@gmail.com'
msg['To'] = COMMASPACE.join(family)
msg.preamble = 'what the..'
pngfiles = ['./img/example.png', './img/example2.png']

for file in pngfiles:
    fp = open(file, 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    img.add_header('Content-Disposition', 'attachment', filename=file)
    msg.attach(img)


s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
s.login(id, passwd)
s.sendmail("",family,msg.as_string())
s.quit()
