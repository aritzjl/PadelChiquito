from django.conf import settings
from email.message import EmailMessage
import ssl
import smtplib
import re
async def send_email_token(email, token):
    try:
        email_emisor = settings.EMAIL_SENDER
        email_contra = settings.EMAIL_PASS
        email_receptor = email
        email_subject = "Bienvenido a Padel Chiquito!"
        email_body = f'Clica aqui para verificar tu cuenta: http://www.padelchiquito.com/verify/{token}'

        em = EmailMessage()
        em["From"] = email_emisor
        em["To"] = email_emisor
        em["Subject"] = email_subject
        em.set_content(email_body)
        contexto = ssl.create_default_context()
        with smtplib.SMTP_SSL("mail1.netim.hosting", 465, context=contexto) as mensaje:
            mensaje.login(email_emisor, email_contra)
            mensaje.sendmail(email_emisor, email_receptor, em.as_string())

    except Exception as e:
        return False
    return True


async def send_recovery_mail(email, token):
    try:
        email_emisor = settings.EMAIL_SENDER
        email_contra = settings.EMAIL_PASS
        email_receptor = email
        email_subject = "Recuperar Contrasena"
        email_body = f'Clica este link para obtener una nueva contrasena: http://www.padelchiquito.com/change-password/{token}'

        em = EmailMessage()
        em["From"] = email_emisor
        em["To"] = email_emisor
        em["Subject"] = email_subject
        em.set_content(email_body)
        contexto = ssl.create_default_context()
        with smtplib.SMTP_SSL(" mail1.netim.hosting", 465, context=contexto) as mensaje:
            mensaje.login(email_emisor, email_contra)
            mensaje.sendmail(email_emisor, email_receptor, em.as_string())
    except Exception as e:
        return False
    return True

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    match = re.match(pattern, email)
    return match is not None