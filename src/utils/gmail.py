from decouple import config
from email.message import EmailMessage
import smtplib
import ssl

def sendGmail(gmailUser, NameUser) :

    gmailSender = config('GMAIL_SENDER')
    gmailPassword = config('GMAIL_KEY')
    gmailReciver = gmailUser

    title = "Bienvenido a Plantz!"
    body = f"""Hola {NameUser}!, Mediante este correo confirmamos su registro en nuestra Web. 
    Esperamos que nuestro producto sea de ayuda y utilidad para usted."""
    
    em = EmailMessage()
    em["From"] = gmailSender
    em["To"] = gmailReciver
    em["Subject"] = title
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as smtp :
        smtp.login(gmailSender, gmailPassword)
        smtp.sendmail(gmailSender, gmailReciver, em.as_string())