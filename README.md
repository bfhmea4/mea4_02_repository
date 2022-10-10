# mea4_02_repository
## Project Description
File Repository Playground is an app intended to run file similarity checks. To find different kind of similarities  
based on multiple criteria.

## Run using Docker
```
docker build -t fileRepo .
docker run --name fileRepo:latest -p 8000:8000 fizzbuzz
```

To use the application open a web browser or use another client and brows to http://0.0.0.0:8000

## Running locally
In order to run the code directly on the machine, one has to install the python modules first.  
After installing the requirements, run the main script:  
```
pip install -r requirements.txt  
python main.py
```
Webserver will be available using: http://localhost:8000

## Invoke REST API

Getting fizzbuzz responses:
Run from locally:
```
curl -X GET http://localhost:8000/1
```

Run from docker:
```
curl -X GET http://0.0.0.0:8000/1
```

## Develop Backend
All backend logic is placed in the ./app folder. To add endpoints or change behaviour one can add/change the code  
written in ./app

## Develop Algorithms 
Adding algorithms unrelated to the backend/frontend calculations, may be achieved by adding/changing  
code in ./algorithms.

## Contributors
Contributions to this project are gladly received, please make sure to send these according to the common contribution guidelines 

