from typing import NamedTuple

class Key(NamedTuple):
    id : int
    value : str
    status : int


def to_key(func) -> object:
    def wrapper(*args, **kwargs) -> object:
        try:
            result : list = func(*args, **kwargs)[0]
        except:
            return []
        return Key(
            id = result[0],
            value = result[1],
            status = result[2],
        )
    return wrapper

def to_keys(func) -> object:
    def wrapper(*args, **kwargs) -> object:
        result : list = func(*args, **kwargs)
        keys : list = []
        for key in result:
            keys.append(Key(
                id = key[0],
                value = key[1],
                status = key[2],
            ))
        return keys
    return wrapper