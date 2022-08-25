import sqlite3
# from venv import create

def create_db():
    con = sqlite3.connect(r"yms.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee (eid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, address TEXT, gender TEXT, DOB TEXT, password TEXT, contact TEXT, DOJ TEXT, user_type TEXT, salary TEXT)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS supplier (invoice INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, contact TEXT, desc TEXT)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS catagory (c_id INTEGER PRIMARY KEY AUTOINCREMENT, cat_name TEXT)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS product (p_id TEXT , Category TEXT, Supplier TEXT, name TEXT, mrp TEXT, dp TEXT, qty TEXT, status TEXT)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS setting (name TEXT, phone_no TEXT, address TEXT, discount TEXT, email TEXT, website TEXT, image BOLB)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS customer (cus_name TEXT, customer_bill TEXT, payment TEXT, paid TEXT, p_name TEXT, product_qty TEXT)")
    con.commit()

create_db()
