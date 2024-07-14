from string import ascii_uppercase
from random import randint
from os import path, getcwd
from threading import Thread
from services.database.database import db
from services.database.keys import Key, to_key, to_keys

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
    users_keys : list = [generate_key() for x in range(0, 9)]
    
    Thread(target = insert_into_file, args = [root_key, users_keys, counter,]).start()
    insert_into_db(keys = [root_key], status = 1)
    Thread(target = insert_into_db, args = [users_keys, 0,]).start()

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
    query_values : str = ", ".join(f"('{key}', {status})" for key in keys)
    db.execute(f"INSERT INTO keys (value, status) VALUES {query_values}", is_commit=True)


for i in range(0, 100000):
    Thread(target = generate_pack, args = [i,]).start()

# @to_keys
# def get_keys() -> list:
#     return db.execute("SELECT * FROM keys")

# @to_key
# def get_key(id : int) -> list:
#     return db.execute("SELECT * FROM keys WHERE id='{}'".format(id))

# print(db.execute("SELECT * FROM keys"))
# print(get_keys())
# print(get_key(id = 5))