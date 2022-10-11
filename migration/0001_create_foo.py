#
# file: migration/0001_create_foo.py
#
from yoyo import step


def apply_step(conn):
    cursor = conn.cursor()
    cursor.execute(
        '''
    CREATE TABLE fizzbuzz
    (id INTEGER PRIMARY KEY ASC, request int, response varchar(50))
''')


def rollback_step(conn):
    cursor = conn.cursor()
    cursor.execute(
        # query to undo the above
    )


steps = [
    step(apply_step, rollback_step)
]
