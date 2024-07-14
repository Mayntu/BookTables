from typing import NamedTuple
from services.database.database import db

class Product(NamedTuple):
    id : int
    author : int
    title : str
    content : str
    date : str


def insert_new_product(data : dict) -> int:
    try:
        
        db.execute(
            query = "INSERT INTO products(author, title, content, date) VALUES ({}, '{}', '{}', '{}')".format(
                data["author"],
                data["title"],
                data["content"],
                data["date"],
            ),
            is_commit = True,
        )
        return 0
    except Exception as e:
        print(e)
        return 1
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


def get_products_by_id(id : int) -> dict:
    products : list[Product] = get_all_products_by_author(
        author_id = id,
    )

    for product in products:
        product = product._asdict
    return products

@to_products
def get_all_products_by_author(author_id : int) -> list[Product]:
    return db.execute("SELECT * FROM products WHERE author={}".format(author_id))


def get_products_by_company(company : str) -> dict:
    products : list[Product] = get_all_products_by_company(
        company = company,
    )
    
    for product in products:
        product = product._asdict
    return products


@to_products
def get_all_products_by_company(company : str) -> list[Product]:
    users = db.execute(f"SELECT * FROM users WHERE company='{company}'")
    print(users)
    products : list = []
    for user in users:
        print(user)
        products.append(db.execute("SELECT * FROM products WHERE author={}".format(user[0])))
    
    products2 : list = []
    for i in products:
        for j in i:
            products2.append(j)

    print(products2)
    return products2


def delete_product_by_id(id : int) -> int:
    return db.execute(query = "DELETE FROM products WHERE id={}".format(id))