# Documentation
(For this website go to: https://bfhmea4.github.io/mea4_02_repository/)

## File repository project
This project aimes to create a container where files can be uploaded and systematically searched for similarities based on different definitions. It's main purpose is to detect and show files of any kind which are similar compared to other files.

## Running/Installation
### Running using Python
#### Backend
In Order to run the backend one needs to install all pip requiremtns listed in requirements.txt:
`````
pip install -r requirements
`````
After installing the requirements the main.py can be executed, starting the FastAPI backend:
`````
python main.py
`````
The backend is now available usinng: http://127.0.0.1:8000

### Running using Docker
There is also a dockerized version of our filerepo, one can either built it from scratch (Dockerfile) or download the latest image from dockerhub.
Running in root directory:
`````
docker build -t fileRepo .
docker run --name fileRepo:latest -p 8000:8000 fileRepo
`````
Running from docker hub:
`````
docker pull hu6li/mea4_02_repository:latest
docker run -it --name filerepo -p 8000:8000 hu6li/mea4_02_repository
`````
The backend is now available usinng: http://0.0.0.0:8000


## Invoke REST API
* Upload file to repo:
`````
curl -X POST http://localhost:8000/files -F file=@/path/to/file.dat
`````
* Get files in repo:
`````
curl -X GET http://localhost:8000/files
`````
* Get file info:
`````
curl -X GET http://localhost:8000/files/{fileID}/info
`````
* Download specific file:
`````
curl -X GET http://localhost:8000/files/{fileID}
`````
* Delete specific file:
`````
curl -X DELETE http://localhost:8000/files/{fileID}
`````

## Frontend
The frontend (UI) is realized using angular and interacts with the backend. The default path for the backend is set to be:  
`````
# /filerepo/frontend/filerepo/src/app/filerepo.service.ts
'http://127.0.0.1:8000/files';
`````

### Running frontend
To run the frontend and successfully interact with it, one must first run the backend and then start the frontend:
brows into /filerepo/frontend/filerepo
`````
ng serve
`````


## Project overview
- Scrum
  [Go to Srum](https://bfhmea4.github.io/mea4_02_repository/scrum/scrum)
- First Sprint
  [First Sprint](https://bfhmea4.github.io/mea4_02_repository/sprint1/sprint1)
- Second Sprint
  [Second Sprint](https://bfhmea4.github.io/mea4_02_repository/sprint2/sprint2)
- User Documentation
  [User Documentation](https://bfhmea4.github.io/mea4_02_repository/userdocu/userdocumentation)