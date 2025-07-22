# 💸 QuickBill - Flask Billing Application

QuickBill is a modern, intuitive billing management system crafted with **Flask**, **SQLite**, and **Bootstrap**.  
Designed for simplicity and speed, it lets you manage customers, products, bills, and history through a beautiful responsive interface.

---

## ✨ Features

- **👥 Customer Management:** Add, edit, and track all your customers in one place.
- **🛒 Product Catalog:** Add multiple products at once, manage inventory, and view product lists.
- **🧾 Bill Generation:** Create professional bills, download them as text files, and auto-save to your database.
- **🔍 Bill Search:** Instantly locate bills using Bill ID.
- **📜 Bill History:** Browse, filter, and view past transactions in a sleek table.
- **📱 Responsive UI:** Experience seamless usage across mobile, tablet, and desktop devices.
- **🚀 Modern Bootstrap Design:** Enjoy a clean, user-friendly interface powered by Bootstrap.

---

## 🛠️ Tech Stack

| Layer      | Technology               |
|------------|--------------------------|
| Frontend   | HTML, CSS, Bootstrap     |
| Backend    | Flask (Python)           |
| Database   | SQLite                   |
| Utilities  | Flask-Cors, Gunicorn     |

---

## 📂 Folder Structure

```
Billing_Application_Flask/
│
├── app.py
├── bill_app.db
├── requirements.txt
├── Procfile
│
├── static/
│   └── exp.mp4
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add_customer.html
│   ├── add_product.html
│   ├── generate_bill.html
│   ├── search_bill.html
│   └── bill_history.html
│
└── database/
    ├── __init__.py
    ├── database.py
    └── models.py
```

---

## ⚡ Quick Start

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/QuickBill-Flask-App.git
cd QuickBill-Flask-App
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Launch the Application

```bash
python app.py
```

The app will be available at [http://localhost:5000](http://localhost:5000).

---

## 🖼️ Screenshots

<div align="center">

### 🏠 Dashboard
<img width="1359" height="620" alt="Screenshot (386)" src="https://github.com/user-attachments/assets/c88b8f36-f064-481d-96c0-b55e2e70a51c" />


</div>

---

## 🙋‍♂️ Author

**Gous13**

- [GitHub Profile](https://github.com/Gous13)
- [LinkedIn](https://www.linkedin.com/in/gous13/)


---


> _QuickBill — Fast. Simple. Reliable Billing for Everyone!_
