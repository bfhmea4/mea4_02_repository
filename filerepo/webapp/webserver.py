import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from filerepo.webapp.repository.database import create_tables
from filerepo.webapp.routers import files, fizzbuzz, upload_activity

origins = ["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

create_tables()

def run():
    uvicorn.run("filerepo.webapp.webserver:app", port=8000, log_level="debug")


app.include_router(files.router)
app.include_router(upload_activity.router)
app.include_router(fizzbuzz.router)


# Kann man auch auf Command Line machen
if __name__ == "__main__":
    run()
