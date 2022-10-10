FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY app /code/app
COPY algorithms /code/algorithms

EXPOSE 8000

CMD ["uvicorn", "app.webserver:app", "--host", "0.0.0.0", "--port", "8000"]
