SENHA = open('./Modulo 2/Semana 1/Dia2/SENHA', 'r').read()

from email.message import EmailMessage
import smtplib
import ssl
import mimetypes

from_email = 'heliofreislima@gmail.com'
to_email = 'helio_lima@outlook.com.br'
subject = 'Mensagem HTML'
body = open('./Modulo 2/Semana 1/Dia2/index.html.txt', 'r', encoding='utf-8').read()

message = EmailMessage()

message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject
message.set_content(body, subtype='html')

safe = ssl.create_default_context()
anexo = './Modulo 2/Semana 1/Dia2/corpo.txt'

mime_type, mime_subtype = mimetypes.guess_type(anexo)[0].split('/')

with open(anexo, 'rb') as anexo:
    message.add_attachment(anexo.read(), 
                           maintype=mime_type, 
                           subtype=mime_subtype, 
                           filename=anexo.name)
    
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as server:
    server.login(from_email, SENHA)
    server.sendmail(from_email, to_email, message.as_string())