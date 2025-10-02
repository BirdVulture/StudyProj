#sqlite3
#.open products.db
#CREATE TABLE products (Id INTEGER, name TEXT NOT NULL, calories INTEGER NOT NULL, PRIMARY KEY(Id));
#INSERT INTO products (Id, name, calories) VALUES ("1", "milk", "2")
#SELECT * FROM products
#.schema


class prodModel:
    def __init__(self, prodId, prodName, cal):
        self.prodId = prodId
        self.name = prodName
        self.cal = cal

