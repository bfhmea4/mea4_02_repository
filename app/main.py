import venv

import sqlite3
import fastapi
import uvicorn
import fizzbuzz.fizzbuzz as fizzbuzz

app = fastapi.FastAPI()


def apply_step():
    conn = sqlite3.connect('/C:/Users/bernh/git/pycharm/mea4_02_repository/data/db/db.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE fizzbuzz
    (id INTEGER PRIMARY KEY ASC, request int, response varchar(50))
''')
    conn.commit()
    conn.close()


# Kann man auch auf Command Line machen
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="debug")

apply_step()


@app.get("/{number}")
def read_item(number: int):
    return {"output": fizzbuzz.fizzbuzz(number)}
