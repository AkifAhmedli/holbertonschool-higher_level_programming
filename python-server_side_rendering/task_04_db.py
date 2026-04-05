import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# JSON oxuma funksiyası
def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

# CSV oxuma funksiyası
def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

# SQL oxuma funksiyası
def read_sql():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        # Bu sətir nəticələri lüğət kimi almağa imkan verir
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        rows = cursor.fetchall()
        # Row obyektlərini standart dict-ə çeviririk
        products = [dict(row) for row in rows]
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    # Mənbə seçimi
    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        data = read_sql()
    else:
        return render_template('product_display.html', error="Wrong source")

    # ID-yə görə filtrasiya
    if product_id:
        filtered_data = [p for p in data if p['id'] == product_id]
        if not filtered_data:
            return render_template('product_display.html', error="Product not found")
        data = filtered_data

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
