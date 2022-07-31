import sqlite3
from sqlite3 import Error


def create_connection(db):
    conn = None
    try:
        conn = sqlite3.connect(db)
    except Error as e:
        print(e)

    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)


def create_product(conn, product):
    try:
        sql = """INSERT INTO products(product_tittle, price, quantity)
        VALUES (?, ?, ?)
        """
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error as e:
        print(e)


def update_quantity(conn, product):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error as e:
        print(e)


def change_price(conn, product):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error as e:
        print(e)


def delete_product(conn, id):
    try:
        sql = """DELETE FROM products WHERE id = ? """
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except Error as e:
        print(e)


def select_and_print_product(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for r in rows:
            print(r)
    except Error as e:
        print(e)


def select_product(conn, limit_price, limit_quantity):
    try:
        sql = """SELECT * FROM products WHERE price <= ? and quantity > ?"""
        cursor = conn.cursor()
        cursor.execute(sql, limit_price, limit_quantity)
        rows = cursor.fetchall()
        for r in rows:
            print(r)
    except Error as e:
        print(e)


def search_product(conn, product_title):
    try:
        sql = """ SELECT * FROM products WHERE product_tittle LIKE ? """
        cursor = conn.cursor()
        cursor.execute(sql, [product_title])
        rows = cursor.fetchall()
        for r in rows:
            print(r)
    except Error as e:
        print(e)


connect = create_connection('''hw.db''')
create_product_table = """CREATE TABLE products(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    product_tittle VARCHAR(200) NOT NULL,
    price DOUBLE (10,2) NOT NULL DEFAULT 0.0,
    quantity INTEGER(5) NOT NULL DEFAULT 0
)"""

if connect is not None:
    print('Connected successfully!')

select_and_print_product(connect)
# select_product(connect, 100, 5)


def add_product():
    create_product(connect, ('Зубная паста', 76, 100))
    create_product(connect, ('Зубная щетка', 55, 150))
    create_product(connect, ('Зубная нить', 90, 250))
    create_product(connect, ('Шампунь', 170, 127))
    create_product(connect, ('Мыло', 30, 37))
    create_product(connect, ('Хоз. мыло', 15, 500))
    create_product(connect, ('Резиновые перчатки', 130, 500))
    create_product(connect, ('Швабра', 700, 30))
    create_product(connect, ('Метла', 320, 50))
    create_product(connect, ('Батарейки', 20, 60))
    create_product(connect, ('Ведро', 67, 47))
    create_product(connect, ('Моющее средство', 490, 700))
    create_product(connect, ('Тазик', 59, 78))
    create_product(connect, ('Краска', 800, 31))
    create_product(connect, ('Лейка', 560, 55))