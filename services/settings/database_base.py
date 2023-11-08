DB_NAME : str = "default.db"

TABLES : dict = {
    "keys" : {
        "id" : "INTEGER PRIMARY KEY AUTOINCREMENT,",
        "value" : "VARCHAR(16) NOT NULL,",
        "status" : "INTEGER NOT NULL",
    },
    "users" : {
        "id" : "INTEGER PRIMARY KEY AUTOINCREMENT,",
        "status" : "INTEGER NOT NULL,",
        "company" : "VARCHAR(16),",
        "email" : "VARCHAR(32) NOT NULL,",
        "password" : "VARCHAR(32) NOT NULL",
    },
    "products" : {
        "id" : "INTEGER PRIMARY KEY AUTOINCREMENT,",
        "author" : "INTEGER NOT NULL,",
        "title" : "VARCHAR(32) NOT NULL,",
        "content" : "VARCHAR(512) NOT NULL,",
        "date" : "VARCHAR(16) NOT NULL",
    },
}