from typing import Annotated
from fastapi import FastAPI, File, UploadFile
from peewee import *

from models import *

db = SqliteDatabase("db/database.db")

app = FastAPI()

with db:
    db.create_tables([Team, User, Task])

    '''@app.post("/check_user")
    async def check_user(email: str):
        users = User.select()
        all_email = [user.email for user in users]
    '''

    #USER

    @app.post("/authorization")
    def authorization(email: str, password: str):
        if User.select().where(User.email == email):
            if User.select().where(User.password == password):
                for user in User.select().where(User.password == password):
                    return "DONE", user

            else:
                return "the password is incorrect"
        else:
            return "the email is incorrect"

    @app.post("/register")
    def register(username: str, name: str, surname: str, email: str, password: str):
        register = [
            {"username": username, "name": name, "surname": surname, "email": email, "password": password,
             "level": 1}
        ]
        User.insert_many(register).execute()
        return "DONE"



    #TASK

    @app.post("/create_task")
    def create_task(name: str, level_count: int, description: str, location: str):
        task = [
            {"name": name, "level_count": level_count, "description": description, "location": location}
        ]
        Task.insert_many(task).execute()

    @app.post("/change_status")
    def change_status1(id_task: int, status: int):
        q = Task.update({Task.status: status}).where(Task.id == id_task)
        q.execute()
        return "DONE"


    @app.get("/get_alltasks")
    def get_all_task():
        return list(Task.select())


    #TEAM

    @app.post("/create_team")
    def check_level(level: int):
        if level >= 5:
            def create_team(name: str):

                team = [
                    {"name": name} # !!! need to add a list of team members
                ]
                Team.insert_many(team).execute()
        else:
            return "sorry, the team can be created from 5 level"

    @app.get("/get_allteams")
    def get_all_teams():
        return list(Team.select())


    #CHECK TASK(FOR ADMIN)

    @app.post("/response_task")
    def response_task(descriprion: str, task: list, user: list):
        check_task = [
            {"descriprion": descriprion, "task": task, "user": user}
        ]
        Team.insert_many(check_task).execute()


    @app.get("/get_allchecktasks")
    def get_all_check_task():
        return list(Check_Task.select())



    # USER_PROFILE

    @app.post("/get_user_profile")
    def get_user_profile(user_id: int):
        return list(User.select().where(User.id == user_id))


    #PLAY

    @app.post("/get_user_level")
    def get_user_level(user_id: int):
        for user in User.select().where(User.id == user_id):
            return user.level


    @app.post("/change_level")
    def change_level(user_id: int):
        q = User.update({User.level: User.level + 1}).where(User.id == user_id)
        q.execute()



    '''@app.post("/files/")
    async def create_file(file: Annotated[bytes, File()]):
        return {"file_size": len(file)}


    @app.post("/uploadfile/")
    async def create_upload_file(file: UploadFile):
        avatar = file.filename'''

