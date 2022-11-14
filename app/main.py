from fastapi import FastAPI
from fastapi_mail import MessageSchema, MessageType, FastMail
from pydantic import EmailStr, BaseModel
from starlette.background import BackgroundTasks
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from .database import ref
from .helpers import generate_id

from .send_email import conf
from typing import List


class User(BaseModel):
    """ Todo schema """
    user_id: str = ""
    name: str = ""
    email: str = ""
    gender: str = ""
    region: str = ""
    constituency: str = ""
    person_with_disability: str = ""
    describe_disability: str = ""
    innovation_name: str = ""
    category: str = ""
    entry_type: str = ""
    innovation_period: str = ""
    team_members: list = []
    founder_age: str = ""
    project_description: str = ""
    problem_targeted: str = ""
    current_solution: str = ""
    target_market: str = ""
    twitter: str = ""
    facebook: str = ""
    linkedin: str = ""
    github_profile: str = ""


route = FastAPI()

origins = ["*"]

route.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class EmailSchema(BaseModel):
   email: List[EmailStr]

class EmailContent(BaseModel):
    message: str
    subject: str


# async def send_email_asynchronous():
#     await send_email_async('Hello World','g.abduba43@gmail.com',
#     {'title': 'Hello World', 'name': 'John Doe'})
#     return 'Success'
# @route.get('/send-email/backgroundtasks')
# def send_email_backgroundtasks(background_tasks: BackgroundTasks):
#     send_email_background(background_tasks, 'Hello World',
#     'g.abduba43@gmail.com', {'title': 'Hello World', 'name':       'John Doe'})
#     return 'Success





@route.post('/send-email/asynchronous')
def send_mail(content: EmailContent):
    template = """
           <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
    <div style="width: 100%; background: #efefef; border-radius: 10px; padding: 10px;">
      <div style="margin: 0 auto; width: 90%; text-align: center;">
        <h1 style="background-color: rgba(0, 53, 102, 1); padding: 5px 10px; border-radius: 5px; color: white;">{{ body.title }}</h1>
        <div style="margin: 30px auto; background: white; width: 40%; border-radius: 10px; padding: 50px; text-align: center;">
          <h3 style="margin-bottom: 100px; font-size: 24px;">{{ body.name }}!</h3>
          <p style="margin-bottom: 30px;">Your application has been received successfully. We will get in touch with you.</p>
          <a style="display: block; margin: 0 auto; border: none; background-color: rgba(255, 214, 10, 1); color: white; width: 200px; line-height: 24px; padding: 10px; font-size: 24px; border-radius: 10px; cursor: pointer; text-decoration: none;"
            href="https://fastapi.tiangolo.com/"
            target="_blank"
          >
            Let's Go
          </a>
        </div>
      </div>
    </div>
    </body>
    </html>
            """


    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients= "g.abduba43@gmail.com",  # List of recipients, as many as you can pass
        body=template,
        subtype="html"
    )

    fm = FastMail(conf)
    fm.send_message(message)
    print("Guyo", message)


    return {"message": "user Email Sent!"}

@route.post("/register")
def register(user: User):
    content = EmailContent
    user_dict = user.dict()
    if user:
        user_id = generate_id()
        user_dict.update({"user_id": user_id})
        # send_mail(content,user.email)
        ref.child(user_id).set(user_dict)
        return {"message": "user registered!"}


@route.get("/users")
async def get_users():
    try:
        users = [value for value in ref.get().values()]
        return {"users": users}
    except Exception as e:
        return {"users": []}
