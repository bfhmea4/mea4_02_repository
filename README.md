# mea4_02_repository
## Project Description
File Repository Playground is an app intended to run file similarity checks. To find different kind of similarities  
based on multiple criteria.

## Run using Docker
```
docker build -t fileRepo .
docker run fileRepo:latest -p 8000:8000
```

To use the application open a web browser or use another client and brows to http://localhost:8000

## Running locally
In order to run the code directly on the machine, one has to install the python modules first.  
After installing the requirements, run the main script inside the app directory:  
```
pip install -r requirements.txt  
PYTHONPATH=./ python app/main.py
```
Note: Currently the PYTHONPATH variable has to point to the root directory.

## Invoke REST API

Getting fizzbuzz responses:

```
curl -X GET http://localhost:8000/1
```

## Develop Backend
All backend logic is placed in the ./app folder. To add endpoints or change behaviour one can add/change the code  
written in ./app

## Develop Algorithms 
Adding algorithms unrelated to the backend/frontend calculations, may be achieved by adding changing  
code in (currelntly) ./fizzbuzz.  
This will change soon and will be updated here as soon as the change happened.

## Contributors
Contributions to this project are gladly welcomed, please make sure to send these according to the common contribution guidelines 

