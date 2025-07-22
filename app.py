from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from database.database import init_db, get_db_connection
from database.models import add_customer, get_customers, add_product, get_products_by_customer, get_bill_history
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = "bill_secret"

# Ensure bills folder exists
if not os.path.exists("bills"):
    os.makedirs("bills")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer_route():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']
        email = request.form['email']
        add_customer(name, mobile, email)
        flash("Customer added successfully!")
        return redirect(url_for('index'))
    return render_template('add_customer.html')

@app.route('/view_customers')
def view_customers():
    customers = get_customers()
    return render_template('view_customers.html', customers=customers)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product_route():
    customers = get_customers()
    if request.method == 'POST':
        customer_id = request.form['customer']
        product_name = request.form['product_name']
        category = request.form['category']
        price = request.form['price']
        add_product(customer_id, product_name, category, float(price))
        flash("Product added successfully!")
        return redirect(url_for('index'))
    return render_template('add_product.html', customers=customers)

@app.route('/get_products/<int:customer_id>')
def get_products_route(customer_id):
    products = get_products_by_customer(customer_id)
    products_list = [{"id": p["id"], "product_name": p["product_name"], "price": p["price"]} for p in products]
    return jsonify(products_list)

@app.route('/generate_bill', methods=['GET', 'POST'])
def generate_bill():
    customers = get_customers()

    if request.method == 'POST':
        customer_id = request.form['customer']
        selected_products = request.form.getlist('product')
        quantities = request.form.getlist('quantity')

        conn = get_db_connection()
        total = 0
        items = []
        for i, pid in enumerate(selected_products):
            product = conn.execute("SELECT * FROM products WHERE id = ?", (pid,)).fetchone()
            qty = int(quantities[i])
            total += product['price'] * qty
            items.append((product['product_name'], qty, product['price']))

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur = conn.cursor()
        cur.execute("INSERT INTO bills (customer_id, total, date) VALUES (?, ?, ?)",
                    (customer_id, total, date))
        bill_id = cur.lastrowid

        for item in items:
            cur.execute("INSERT INTO bill_items (bill_id, product_name, quantity, price) VALUES (?, ?, ?, ?)",
                        (bill_id, item[0], item[1], item[2]))

        conn.commit()
        conn.close()

        filename = f"bills/BILL_{bill_id}.txt"
        with open(filename, "w") as f:
            f.write(f"Bill ID: {bill_id}\nDate: {date}\nTotal: {total}\n\nItems:\n")
            for item in items:
                f.write(f"{item[0]} - {item[1]} x {item[2]} = {item[1] * item[2]}\n")

        return render_template('generate_bill.html', customers=customers,
                               popup=True, bill_id=bill_id, total=total,
                               items=items, date=date)

    return render_template('generate_bill.html', customers=customers, popup=False)

@app.route('/bill_history')
def bill_history():
    bills = get_bill_history()
    return render_template('bill_history.html', bills=bills)

@app.route('/search_bill', methods=['GET', 'POST'])
def search_bill():
    bill_data = None
    items = []
    if request.method == 'POST':
        bill_id = request.form['bill_id']
        conn = get_db_connection()
        bill = conn.execute("""
            SELECT bills.bill_id, bills.total, bills.date, customers.name AS customer_name
            FROM bills
            JOIN customers ON customers.id = bills.customer_id
            WHERE bills.bill_id = ?
        """, (bill_id,)).fetchone()

        if bill:
            items = conn.execute("SELECT * FROM bill_items WHERE bill_id = ?", (bill_id,)).fetchall()

        conn.close()
        bill_data = (bill, items)
    return render_template('search_bill.html', bill_data=bill_data)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
