#sqlite3
#.open products.db
#CREATE TABLE products (Id INTEGER, name TEXT NOT NULL, calories INTEGER NOT NULL, PRIMARY KEY(Id));
#INSERT INTO products (Id, name, calories) VALUES ("1", "milk", "2");
#SELECT * FROM products;
#.schema
#.quit
# SELECT * FROM products WHERE name = "milk" поиск по названию продукта
# SELECT * FROM products WHERE id = "1" поиск по id


import dataModel
import sqlite3



class dataBaseManager:
    def __init__(self):
        self.products = sqlite3.connect("products.db")
        self.cursor = self.products.cursor()

    def creadeProduct(self, prod):
        self.cursor.execute("INSERT INTO products (Id, name, calories) VALUES (?,?, ?)", prod)

        self.connection.commit()
        self.products.close()
    
    def getProductInfo(self, prod):
        self.cursor.execute("SELECT INTO products (Id, name, calories) VALUES (?,?, ?)", prod)

        self.connection.commit()
        self.products.close()

       