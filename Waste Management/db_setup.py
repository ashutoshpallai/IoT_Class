import sqlite3

conn = sqlite3.connect('waste_management.db')  # Must match the DB file used in app.py
c = conn.cursor()

# Create the table if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS bins (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        bin_id TEXT NOT NULL,
        location TEXT NOT NULL,
        fill_level INTEGER NOT NULL,
        timestamp TEXT NOT NULL
    )
''')

conn.commit()
conn.close()

print("✅ Database and 'bins' table created successfully.")