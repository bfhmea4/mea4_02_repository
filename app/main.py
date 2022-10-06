from typing import Union
import fastapi
import fizzbuzz.fizzbuzz as fizzbuzz
import uvicorn
import logging


logging.basicConfig(filename="log.txt", level=logging.DEBUG)
app = fastapi.FastAPI()


if __name__ == "__main__":
    logging.info("test")
    uvicorn.run("main:app", port=8000, log_level="debug")

@app.get("/{number}")
def read_item(number: int):
    return {"output": fizzbuzz.fizzbuzz(number)}