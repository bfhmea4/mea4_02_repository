from fastapi import FastAPI, Request
from starlette.responses import JSONResponse


app = FastAPI()


class MyFileNotFoundException(Exception):
    def __init__(self, name: str):
        self.name = name


class MyException(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(MyFileNotFoundException)
async def unicorn_exception_handler(request: Request, exc: MyFileNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"message": f"Item with name: {exc.name} not found"},
    )


@app.exception_handler(MyException)
async def unicorn_exception_handler(request: Request, exc: MyException):
    return JSONResponse(
        status_code=400,
        content={"message": f"Item with name: {exc.name} not found"},
    )
