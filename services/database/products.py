from typing import NamedTuple

class Product(NamedTuple):
    id : int
    author : int
    title : str
    content : str
    date : str


def to_product(func) -> object:
    def wrapper(*args, **kwargs) -> object:
        try:
            result : list = func(*args, **kwargs)[0]
        except:
            return []
        return Product(
            id = result[0],
            status = result[1],
            company = result[2],
            email = result[3],
            password = result[4],
        )
    return wrapper

def to_products(func) -> object:
    def wrapper(*args, **kwargs) -> object:
        result : list = func(*args, **kwargs)
        products : list = []
        for product in result:
            products.append(Product(
                id = product[0],
                author = product[1],
                title = product[2],
                content = product[3],
                date = product[4],
            ))
        return products
    return wrapper