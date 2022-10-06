FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY app /code/app
COPY fizzbuzz /code/fizzbuzz

EXPOSE 8000

ENTRYPOINT ["python"]

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "database\sqlite_create.py"]

