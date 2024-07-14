from services.database.database import db

def register(data : dict) -> int:
    key_status : int = check_if_key_exists(key = data["key"])
    print(key_status)
    if email_is_in_db(data = data) == 0 or key_status == 2:
        return 1
    try:
        result_of_register : str = db.execute(query = "INSERT INTO users (status, company, email, password) VALUES ({}, '{}', '{}', '{}')".format(
                key_status,
                data["company"],
                data["email"],
                data["password"],
            ), is_commit = True)
    except:
        return 2
    
    return result_of_register


def email_is_in_db(data : dict) -> int:
    try:
        is_exists : bool = check_if_email_exists(email = data["email"])
    except:
        return 2
    if is_exists:
        return 0
    return 1


def check_if_email_exists(email : str) -> bool:
    user : list = db.execute(query = f"SELECT * FROM users WHERE email='{email}'")
    return len(user) != 0

def check_if_key_exists(key : str) -> (bool, int):
    key_status : list = db.execute(query = f"SELECT status FROM keys WHERE value='{key}'")
    if len(key) > 0:
        return key_status[0][0]
    return 2

email_is_in_db(data = {
    "email" : "1",
})