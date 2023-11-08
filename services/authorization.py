from services.database.database import db

def register(data : dict) -> int:
    if not is_in_db(data = data) == 0:
        return 1
    try:
        ...
    except:
        return 2
    
    return 0


def is_in_db(data : dict) -> int:
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


is_in_db(data = {
    "email" : "1",
})