import psycopg2

def read_products():
    conn = psycopg2.connect(
        dbname="northwind",
        user="postgres",
        password="password",
        host="localhost"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM products;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def write_product(product_id, product_name, price):
        conn = psycopg2.connect(
            dbname="northwind",
            user="postgres",
            password="password",
            host="localhost"
        )
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO products (product_id, product_name, unit_price) VALUES (%s, %s, %s);",
            (product_id, product_name, price)
        )
        conn.commit()
        cur.close()
        conn.close()

if __name__ == "__main__":
    #read_products()
    write_product(1002, "New Product", 19.99)
    