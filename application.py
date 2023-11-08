from services.database.database import db
from services.database.users import (
    User,
    to_user,
    to_users,
)
from services.registration import register

# print(db.execute("INSERT INTO users (status, company, email, password) VALUES (0, 'a', 'a', 'a')", is_commit = True))
print(db.execute("SELECT * FROM users"))


@to_user
def get_user_by_id(id : int) -> list:
    return db.execute(f"SELECT * FROM users WHERE id='{id}'")


@to_users
def get_users() -> list:
    return db.execute("SELECT * FROM users")

print(get_user_by_id(id = 5))
print(get_users())

print(register(data = {
    "status" : 1,
    "company" : "genius",
    "email" : "aa@gmail.com",
    "password" : "12345",
}))