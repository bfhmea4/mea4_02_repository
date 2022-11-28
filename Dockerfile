FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY filerepo/webapp /code/filerepo/webapp
COPY filerepo/algorithms /code/filerepo/algorithms
COPY filerepo/db/ /code/filerepo/db

EXPOSE 8000

CMD ["uvicorn", "filerepo.webapp.webserver:app", "--host", "0.0.0.0", "--port", "8000"]
