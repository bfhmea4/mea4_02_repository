from typing import Union
import fastapi
import algorithms.fizzbuzz as fizzbuzz
import uvicorn

app = fastapi.FastAPI()

#Kann man auch auf Command Line machen
if __name__ == "__main__":
    run()

def run():
    uvicorn.run("app.webserver:app", port=8000, log_level="debug")

@app.get("/{number}")
def read_item(number: int):
    return {"output": fizzbuzz.fizzbuzz(number)}