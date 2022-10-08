from yoyo import step
import sqlite3


def apply_step():
    conn = sqlite3.connect('data/db.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO fizzbuzz VALUES(1, 'fizz', 3)
''')
    conn.commit()
    conn.close()


def rollback_step(conn):
    cursor = conn.cursor()
    cursor.execute(
        # query to undo the above
    )


steps = [
    step(apply_step, rollback_step)
]

