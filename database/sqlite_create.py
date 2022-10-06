import sqlite3

conn = sqlite3.connect('data/db.db')

c = conn.cursor()

c.execute('''
    CREATE TABLE fizzbuzz
    (id INTEGER PRIMARY KEY ASC, request int, response varchar(50))
''')

conn.commit()
conn.close()
