import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from_add = 'vinamragupta121@gmial.com'
to_add = 'phalodispin@gmial.com'
subject = "hi how aae you"

msg = MIMEMultipart()
msg['From' ] =  from_add
msg['To'] = to_add
msg['subject'] = subject

body = ("hey vinamra here")
msg.attach(MIMEText(body,'plain'))
message = msg.as_string()

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(from_add,'Vinamra@123')
message = "hijgiuh98wfhidhtfgiow3hrsrht"
server.sendmail(from_add,to_add,message)

server.quit()