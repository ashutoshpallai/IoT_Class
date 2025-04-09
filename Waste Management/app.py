from flask import Flask, render_template
import sqlite3
import random
from datetime import datetime

app = Flask(__name__)
DB_FILE = 'waste_management.db'

def insert_random_data():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    bin_id = f"BIN-{random.randint(100, 999)}"
    location = random.choice(["Patia", "Sahid Nagar", "CRP Square", "Master Canteen"])
    fill_level = random.randint(0, 100)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    c.execute('''
        INSERT INTO bins (bin_id, location, fill_level, timestamp)
        VALUES (?, ?, ?, ?)
    ''', (bin_id, location, fill_level, timestamp))

    conn.commit()
    conn.close()

def get_latest_bins():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        SELECT bin_id, location, fill_level, timestamp 
        FROM bins 
        ORDER BY timestamp DESC 
        LIMIT 5
    ''')
    rows = c.fetchall()
    conn.close()
    return rows

@app.route('/')
def index():
    insert_random_data()  
    bins = get_latest_bins()
    return render_template('index.html', bins=bins)

if __name__ == '__main__':
    app.run(debug=True)