from flask import Flask, request, session, redirect, url_for, render_template
import json
from services.database.users import (
    User,
    to_user,
    to_users,
    get_user_by_email,
)
from services.database.products import insert_new_product, get_products_by_company, get_products_by_id, delete_product_by_id
from services.registration import register
from services.authorization import authorize
from services.database.database import db
from datetime import datetime

app : Flask = Flask(__name__)
app.secret_key = "fghg39ugh9eruifh39fh"



@app.route("/", methods=["GET"])
def index():
    if "email" in session:
        return render_template("index.html")
    return redirect(url_for("authorization"))

@app.route("/authorization", methods=["GET"])
def authorization():
    if "email" in session:
        return redirect(url_for("index"))
    return render_template("authorization.html")

@app.route("/registration", methods=["GET"])
def registration():
    if "email" in session:
        return redirect(url_for("index"))
    return render_template("registration.html")

@app.route("/api/v1/registration", methods=["POST"])
def api_registration():
    data : dict = request.get_json()
    print(data)
    register_result : int = register(
        data = data,
    )
    print(register_result)
    if register_result == 0:
        session["email"] = data["email"]
    
    return json.dumps({"result" : register_result})

@app.route("/api/v1/authorization", methods=["POST"])
def api_authorization():
    data : dict = request.get_json()
    print(data)
    authorize_result : int = authorize(
        data = data,
    )
    if authorize_result == 0:
        session["email"] = data["email"]
    
    return json.dumps({"result" : authorize_result})

@app.route("/api/v1/deauth", methods=["POST"])
def deauth():
    if "email" in session:
        session.clear()
        return json.dumps({
            "result" : 0,
            "query"  : "DEAUTH",
        })
    return json.dumps({
        "result" : 1,
        "query"  : "DEAUTH",
    })


@app.route("/api/v1/getAllProducts", methods=["POST"])
def api_get_all_products():
    user : User = get_user_by_email(
        email = session["email"],
    )
    if isinstance(user, User):
        user_id : int = user.id
        user_company : int = user.company
        if user.status == 0:
            return json.dumps({
                "result" : get_products_by_id(id = user_id)
            })
        return json.dumps({
            "result" : get_products_by_company(company = user_company)
        })


@app.route("/api/v1/insertProduct", methods=["POST"])
def api_insert_product():
    data: dict = request.get_json()
    user : User = get_user_by_email(
        email = session["email"],
    )
    if isinstance(user, User):
        user_id : int = user.id
        data["author"] = user_id
        data["date"] = datetime.utcnow().strftime("%M:%Y:%d")
        return json.dumps({
        "result" : insert_new_product(data=data)
    })
    return json.dumps({"result" : 1})


@app.route("/api/v1/deleteProduct", methods=["POST"])
def api_delete_product():
    data: dict = request.get_json()
    return json.dumps({"result" : delete_product_by_id(id = data["id"])})

print(db.execute("SELECT * FROM users"))
print(db.execute("SELECT * FROM users"))
print(db.execute("SELECT * FROM users"))
print(db.execute("SELECT * FROM users"))
print(db.execute("SELECT * FROM users"))
print(db.execute("SELECT * FROM users"))
print(db.execute("SELECT * FROM users"))
print(db.execute("SELECT * FROM users"))
print(db.execute("SELECT * FROM users"))
print(db.execute("SELECT * FROM products"))
print(db.execute("SELECT * FROM products"))
print(db.execute("SELECT * FROM products"))
print(db.execute("SELECT * FROM products"))
print(db.execute("SELECT * FROM products"))
if __name__ == "__main__":
    app.run(debug = True)