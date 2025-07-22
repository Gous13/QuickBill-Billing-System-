from .database import get_db_connection

def add_customer(name, mobile, email):
    conn = get_db_connection()
    conn.execute("INSERT INTO customers (name, mobile, email) VALUES (?, ?, ?)",
                 (name, mobile, email))
    conn.commit()
    conn.close()

def get_customers():
    conn = get_db_connection()
    customers = conn.execute("SELECT * FROM customers").fetchall()
    conn.close()
    return customers

def add_product(customer_id, product_name, category, price):
    conn = get_db_connection()
    conn.execute("INSERT INTO products (customer_id, product_name, category, price) VALUES (?, ?, ?, ?)",
                 (customer_id, product_name, category, price))
    conn.commit()
    conn.close()

def get_products_by_customer(customer_id):
    conn = get_db_connection()
    products = conn.execute("SELECT * FROM products WHERE customer_id=?", (customer_id,)).fetchall()
    conn.close()
    return products

def get_bill_history():
    conn = get_db_connection()
    bills = conn.execute("""
        SELECT bills.bill_id, customers.name, bills.total, bills.date
        FROM bills
        JOIN customers ON customers.id = bills.customer_id
        ORDER BY bills.date DESC
    """).fetchall()
    conn.close()
    return bills
