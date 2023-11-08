from string import ascii_uppercase
from random import randint

NUMS : str = "1234567890"

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

print(generate_key())