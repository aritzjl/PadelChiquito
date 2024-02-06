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
        email_body = f"""
        <html>
            <head>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                        background-color: #f4f4f4;
                        color: #555;
                    }}
                    .container {{
                        max-width: 600px;
                        margin: 20px auto;
                        padding: 20px;
                        background-color: #fff;
                        border-radius: 10px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    }}

                    .button {{
                        display: inline-block;
                        padding: 10px 20px;
                        background-color: #39FF14;
                        color: #000;
                        text-decoration: none;
                        border-radius: 5px;
                        font-weight: bold;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h2>Verificación de Cuenta</h2>
                    <p>Hola,</p>
                    <p>Por favor, verifica tu cuenta clicando en el botón abajo:</p>
                    <a href="https://www.padelchiquito.com/verify/{token}" class="button">Verifica tu cuenta</a>
                    <p>Gracias por unirte a nosotros. ¡Estamos emocionados de tenerte a bordo!</p>
                </div>
            </body>
        </html>
        """

        em = EmailMessage()
        em["From"] = email_emisor
        em["To"] = email_emisor
        em["Subject"] = email_subject
        em.set_content(email_body, subtype='html')
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
        email_body = f"""
        <html>
            <head>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                        background-color: #f4f4f4;
                        color: #555;
                    }}
                    .container {{
                        max-width: 600px;
                        margin: 20px auto;
                        padding: 20px;
                        background-color: #fff;
                        border-radius: 10px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    }}
                    .button {{
                        display: inline-block;
                        padding: 10px 20px;
                        background-color: #39FF14;
                        color: #000;
                        text-decoration: none;
                        border-radius: 5px;
                        font-weight: bold;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h2>Recuperación de Contraseña</h2>
                    <p>Hola,</p>
                    <p>Clica el siguiente enlace para restablecer tu contraseña:</p>
                    <a href="https://www.padelchiquito.com/change-password/{token}" class="button">Restablecer Contraseña</a>
                    <p>Si no solicitaste esta acción, puedes ignorar este correo.</p>
                </div>
            </body>
        </html>
        """

        em = EmailMessage()
        em["From"] = email_emisor
        em["To"] = email_emisor
        em["Subject"] = email_subject
        em.set_content(email_body, subtype='html')
        contexto = ssl.create_default_context()
        with smtplib.SMTP_SSL("mail1.netim.hosting", 465, context=contexto) as mensaje:
            mensaje.login(email_emisor, email_contra)
            mensaje.sendmail(email_emisor, email_receptor, em.as_string())
    except Exception as e:
        return False
    return True

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    match = re.match(pattern, email)
    return match is not None