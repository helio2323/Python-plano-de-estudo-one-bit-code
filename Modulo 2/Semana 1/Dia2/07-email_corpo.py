SENHA = open('./Modulo 2/Semana 1/Dia2/SENHA', 'r').read()

from email.message import EmailMessage
import smtplib
import ssl

from_email = 'heliofreislima@gmail.com'
to_email = 'helio_lima@outlook.com.br'
subject = 'Boas vindas'
body = open('./Modulo 2/Semana 1/Dia2/corpo.txt', 'r', encoding='utf-8').read()

message = EmailMessage()

message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject
message.set_content(body)

safe = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as server:
    server.login(from_email, SENHA)
    server.sendmail(from_email, to_email, message.as_string())