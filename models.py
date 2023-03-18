from peewee import *

db = SqliteDatabase('db/database.db')


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'


class User(BaseModel):
    username = CharField(unique=True)
    name = CharField()
    surname = CharField()
    email = CharField(unique=True)
    password = CharField()
    level = CharField()


    class Meta:
        db_table = 'users'

class Task(BaseModel):
    name = CharField()
    level_count = IntegerField()
    description = CharField()
    location = CharField()
    status = IntegerField(default=0 or 1 or 2)

    class Meta:
        db_table = 'tasks'

class Team(BaseModel):
    name = CharField()
    user_id = ForeignKeyField(User)

    class Meta:
        db_table = 'teams'