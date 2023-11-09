from string import ascii_uppercase
from random import randint
from os import path, getcwd
from services.database.database import db

NUMS : str = "1234567890"

FILE_PATH : str = path.abspath(getcwd()) + "/keys/"
FILE_NAME : str = "keys#"
FILE_TYPE : str = ".txt"
FILE_CONTENT : str = '''ROOT:
{}

USERS:
'''

def generate_pack(counter : int):
    root_key : str = generate_key()
    users_keys : list = []
    for i in range(0, 9):
        users_keys.append(generate_key())
    
    insert_into_file(
        root_key = root_key,
        users_keys = users_keys,
        counter = counter,
    )
    insert_into_db(keys = [root_key], status = 1)
    insert_into_db(keys = users_keys, status = 0)
def generate_key() -> str:
    key : str = ""
    for i in range(1, 30):
        if i % 6 == 0:
            key += "-"
            continue
        
        if randint(0, 1) == 0:
            key += ascii_uppercase[randint(0, len(ascii_uppercase) - 1)]
        else:
            key += NUMS[randint(0, len(NUMS) - 1)]
    
    return key

def insert_into_file(root_key : str, users_keys : list, counter) -> None:
    file = open(file = f"{FILE_PATH}{FILE_NAME}{counter}{FILE_TYPE}", mode = "w")
    
    file_data : str = FILE_CONTENT.format(root_key)
    for user_key in users_keys:
        file_data += user_key + "\n"
    
    file.write(file_data)
    file.close()


def insert_into_db(keys : list, status : int) -> None:
    for key in keys:
        db.execute(query = "INSERT INTO keys (value, status) VALUES ('{}', {})".format(key, status))


for i in range(0, 1000):
    generate_pack(counter = i)
print(db.execute("SELECT * FROM keys"))