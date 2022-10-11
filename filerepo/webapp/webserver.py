from typing import Union
import fastapi
import filerepo.algorithms.fizzbuzz as fizzbuzz
import uvicorn

app = fastapi.FastAPI()

def run():
    uvicorn.run("filerepo.webapp.webserver:app", port=8000, log_level="debug")

@app.get("/{number}")
def read_item(number: int):
    return {"output": fizzbuzz.fizzbuzz(number)}

#Kann man auch auf Command Line machen
if __name__ == "__main__":
    run()