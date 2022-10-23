from fastapi import APIRouter
from fastapi.responses import JSONResponse, FileResponse
import filerepo.algorithms.fizzbuzz as fizzbuzz



router = APIRouter()

@router.get("/fizzbuzz/{number}", tags=["fizzbuzz"])
def read_item(number: int):
    return {"output": fizzbuzz.fizzbuzz(number)}