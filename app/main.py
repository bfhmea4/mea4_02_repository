import sqlite3
import fastapi
import uvicorn

import fizzbuzz.fizzbuzz as fizzbuzz
from migration.post import Repo

app = fastapi.FastAPI()





# Kann man auch auf Command Line machen
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="debug")

# Repo.create_table_fizzbuzz();
Repo.fizzpuzz_post(3, 3, "fizz")


@app.get("/{number}")
def read_item(number: int):
    return {"output": fizzbuzz.fizzbuzz(number)}
