# mea4_02_repository
## Project Description
File Repository Playground is an app intended to run file similarity checks. To find different kind of similarities  
based on multiple criteria.

## Run using Docker
```
docker build -t fileRepo .
docker run --name fileRepo:latest -p 8000:8000 fileRepo
```

Or download it directly from docker hub:

```
docker pull hu6li/mea4_02_repository:latest
docker run -it --name filerepo -p 8000:8000 hu6li/mea4_02_repository
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

Getting responses:
Run get files command from locally:
```
curl -X GET http://localhost:8000/files
```

Run get files command from docker:
```
curl -X GET http://0.0.0.0:8000/files
```

Upload a file:
```
curl -X 'POST' -F file=@/path/to/file http://localhost:8000/files/upload
```

## Develop Backend
```
├── Dockerfile
├── docu
│   └── canvas.png
├── filerepo
│   ├── algorithms
│   │   ├── fizzbuzz.py
│   │   └── __init__.py
│   ├── tests
│   │   ├── algorithm_fizzbuzz
│   │   │   └── test_fizz_buzz.py
│   │   ├── __init__.py
│   │   └── webserver_api
│   │       ├── test_delete_api.py
│   │       ├── test_download_file.py
│   │       ├── test_fileInfo_api.py
│   │       ├── test_fizz_buzz_api.py
│   │       ├── test_get_files_api.py
│   │       └── test_upload_api.py
│   └── webapp
│       ├── database
│       │   ├── file
│       │   │   ├── file_dto.py
│       │   │   ├── file_repository.py
│       │   │   └── __init__.py
│       │   ├── file_system.py
│       │   └── __init__.py
│       ├── domain
│       │   ├── file
│       │   │   ├── file_exception.py
│       │   │   ├── file.py
│       │   │   ├── file_repository.py
│       │   │   └── __init__.py
│       │   └── __init__.py
│       ├── __init__.py
│       ├── routers
│       │   ├── files.py
│       │   ├── fizzbuzz.py
│       │   └── __init__.py
│       ├── schemas
│       │   └── file_schema.py
│       ├── service
│       │   ├── file_service.py
│       │   └── __init__.py
│       └── webserver.py
├── main.py
├── pyproject.toml
├── README.md
└── requirements.txt
```
All backend logic is placed in the ./filerepo/webapp folder. 
To add endpoints use the directory routers and create new routers if the endpoint concerns a new entity else  
add an endpoint to an existing entity.

Database logic is implemented under ./filerepo/webapp/database, it is the place where DTOs are defined and where 
file/DB access happens

To create a new entity use ./filerepo/webapp/domain, keep in mind that the repo classes are only abstract classes and  
the implementation of those classes will be in the database directory

Use the ./filerepo/webapp/schemas directory to create and define models which will be communicated towards the external user.

Finally, use the ./filerepo/webapp/service as interface to communicate between repositories and endpoints. 

## Contributors
Contributions to this project are gladly received, please make sure to send these according to the common contribution guidelines 

