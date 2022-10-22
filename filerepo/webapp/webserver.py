from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from .routers import files, fizzbuzz
import uvicorn
from pathlib import Path
import os

app = FastAPI()

def run():
    uvicorn.run("filerepo.webapp.webserver:app", port=8000, log_level="debug")


app.include_router(files.router)
app.include_router(fizzbuzz.router)


# Kann man auch auf Command Line machen
if __name__ == "__main__":
    run()
