from typing import NamedTuple
from services.database.database import db

class User(NamedTuple):
    id : int
    status : int
    company : str
    email : str
    password : str


def to_user(func) -> object:
    def wrapper(*args, **kwargs) -> object:
        try:
            result : list = func(*args, **kwargs)[0]
        except:
            return []
        return User(
            id = result[0],
            status = result[1],
            company = result[2],
            email = result[3],
            password = result[4],
        )
    return wrapper

def to_users(func) -> object:
    def wrapper(*args, **kwargs) -> object:
        result : list = func(*args, **kwargs)
        users : list = []
        for user in result:
            users.append(User(
                id = user[0],
                status = user[1],
                company = user[2],
                email = user[3],
                password = user[4],
            ))
        return users
    return wrapper

@to_user
def get_user_by_email(email : str) -> User:
    return db.execute("SELECT * FROM users WHERE email='{}'".format(email))