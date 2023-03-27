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






    '''@app.post("/files/")
    async def create_file(file: Annotated[bytes, File()]):
        return {"file_size": len(file)}


    @app.post("/uploadfile/")
    async def create_upload_file(file: UploadFile):
        avatar = file.filename'''

