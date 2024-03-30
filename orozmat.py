import sqlite3

def create_database():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY,
                        product_title TEXT NOT NULL CHECK (product_title != ''),
                        price FLOAT NOT NULL DEFAULT 0.0 CHECK (price >= 0),
                        quantity INTEGER NOT NULL DEFAULT 0 CHECK (quantity >= 0)
                        )''')

    conn.commit()
    conn.close()

def add_product(product_title, price, quantity):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO products (product_title, price, quantity)
                      VALUES (?, ?, ?)''', (product_title, price, quantity))

    conn.commit()
    conn.close()

create_database()

add_product("Яблоко", 20.5, 18)
add_product("Банан", 15.0, 25)