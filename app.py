from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
DATABASE = 'database.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with app.app_context():
        db = get_db()
        db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER
            )
        ''')
        db.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL
            )
        ''')
        db.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def users():
    db = get_db()
    users = db.execute('SELECT * FROM users').fetchall()
    return render_template('users.html', users=users)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        db = get_db()
        db.execute('INSERT INTO users (name, email, age) VALUES (?, ?, ?)',
                   (name, email, age))
        db.commit()
        return redirect(url_for('users'))
    return render_template('add_user.html')

@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    db = get_db()
    db.execute('DELETE FROM users WHERE id = ?', (user_id,))
    db.commit()
    return redirect(url_for('users'))

@app.route('/products')
def products():
    db = get_db()
    products = db.execute('SELECT * FROM products').fetchall()
    return render_template('products.html', products=products)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        quantity = request.form['quantity']
        db = get_db()
        db.execute('INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)',
                   (name, price, quantity))
        db.commit()
        return redirect(url_for('products'))
    return render_template('add_product.html')

@app.route('/search_user', methods=['GET', 'POST'])
def search_user():
    results = []
    if request.method == 'POST':
        search_term = request.form['search']
        db = get_db()
        results = db.execute('SELECT * FROM users WHERE name LIKE ?', 
                            (f'%{search_term}%',)).fetchall()
    return render_template('search_user.html', results=results)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)