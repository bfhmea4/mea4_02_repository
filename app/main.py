import fastapi
import fizzbuzz.fizzbuzz as fizzbuzz
import database
import sqlite3
import uvicorn

app = fastapi.FastAPI()

# Kann man auch auf Command Line machen
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="debug")


@app.get("/{number}")
def read_item(number: int):
    # database.post.apply_step()
    return {"output": fizzbuzz.fizzbuzz(number)}



