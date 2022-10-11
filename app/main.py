import venv

import data as data
import fastapi
import uvicorn
import fizzbuzz.fizzbuzz as fizzbuzz

app = fastapi.FastAPI()

# Kann man auch auf Command Line machen
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="debug")

venv.data.post.apply_step()


@app.get("/{number}")
def read_item(number: int):
    return {"output": fizzbuzz.fizzbuzz(number)}
