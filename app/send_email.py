import os
from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from dotenv import load_dotenv


class Envs:
    MAIL_USERNAME = "registration@neinnovationweek.co.ke"
    MAIL_PASSWORD = "AJ-V=ph4$F4h"
    MAIL_FROM = "registration@neinnovationweek.co.ke"
    MAIL_PORT = 465
    MAIL_SERVER = "mail.neinnovationweek.co.ke"
    MAIL_FROM_NAME = "North Eastern Innovation Week"


conf = ConnectionConfig(
    MAIL_USERNAME=Envs.MAIL_USERNAME,
    MAIL_PASSWORD=Envs.MAIL_PASSWORD,
    MAIL_FROM=Envs.MAIL_FROM,
    MAIL_PORT=Envs.MAIL_PORT,
    MAIL_SERVER=Envs.MAIL_SERVER,
    MAIL_FROM_NAME=Envs.MAIL_FROM_NAME,
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
    # TEMPLATE_FOLDER='app/templates/email'
)


# async def send_email_async(subject: str, email_to: str, body: dict):
#     message = MessageSchema(
#         subject=subject,
#         recipients=[email_to],
#         body=body,
#         subtype=MessageType.html,
#     )

#     fm = FastMail(conf)
#     await fm.send_message(message, template_name='email.html')
#
#
# def send_email_background(background_tasks: BackgroundTasks, subject: str, email_to: str, body: dict):
#     message = MessageSchema(
#         subject=subject,
#         recipients=[email_to],
#         body=body,
#         subtype=MessageType.html,
#     )
    # message = MessageSchema(
    #     subject="Fastapi-Mail module",
    #     recipients=email.dict().get("email"),  # List of recipients, as many as you can pass
    #     body=template,
    #     subtype="html"
    # )
    # fm = FastMail(conf)
    # background_tasks.add_task(
    #     fm.send_message, message, template_name='email.html')