# Sprint 1

## Milestone

### Receive Project Approval
As a team, we look what belongs to this Sprint1 and what doesn't.

### Identify Project Requirements
We have the technology that is given with: docker, fast api, python. 
Then we have the fizzbuzz algorithm, which is given.
The whole process runs according to the specifications of scrum.
  
### Establish Start & End Dates
We have two weeks for this sprint.
Start: thuesday, 27 sep 2022 
End: thuesday, 11 oct 2022

### Scrum init
Decide who takes which role in scrum and show the next steps in the scrum process.
[scrum overview](https://bfhmea4.github.io/mea4_02_repository/scrum/scrum)
z

### Backlog Sprint 
Decide what goes into the backlog sprint and who does what.


### Scrum review
Date: thuesday, 11 oct 2022


### Final approval (end Date)




## Planning for sprint 1

We have determined some tasks and discussed which ones we will include in the backlog for the sprint 1.
[sprint1 backlog](https://github.com/orgs/bfhmea4/projects/4/views/4?layout=board)


### Task: Based on video
[Based on video](https://github.com/bfhmea4/mea4_02_repository/issues/2)

This task works according to the principle and procedure of TDD. Which means that first as simple as possible 
tests are written that fail. Then an attempt is made to improve these tests so that they no longer fail. 
In addition, further cases are processed and at the end it is checked that the algorithm passes all tests.


### Task: RestAPI Tests
[RestApI Tests](https://github.com/bfhmea4/mea4_02_repository/issues/4)

These tests are first written according to the Kata TDD principle, then the Rest API can be built 
and further developed by means of these tests.


### Task: Implementation FizzBuzz Algo in RestAPI
[FizzBuzz Algo](https://github.com/bfhmea4/mea4_02_repository/issues/5)

The rest api is built up and further developed step by step after the rest api test, 
so that all tests run.  If new requests are then installed or adjustments are made, 
it is important that all tests are still running.


### Task: Dockerize the whole thing
[Dockerize](https://github.com/bfhmea4/mea4_02_repository/issues/6)

We create multi-container application using Docker Compose.
Docker creates independent containers of software with virtualization. 
It is then quick and easy to run these containers.


### Task: Install Web documentation
[web docu](https://github.com/bfhmea4/mea4_02_repository/issues/3)

For our documentation we need the tool github pages. 
We create a public branch and structure in this branch our website which runs via github. 
Because it's easier and faster, we write most of it in markdown.


### Task: Scrum init
[scrum init](https://github.com/bfhmea4/mea4_02_repository/issues/7)
Determine who takes over which scrum role. 
Create sprint1 backlog. Update the backlog. 
Check if we are within the scrum guidelines.


### Task: Init Database
[init database](https://github.com/bfhmea4/mea4_02_repository/issues/8)
- Installation

Install yoyo-migrations using from the PyPI, for example:
-> pip install yoyo-migrations

Create a local DB
-> C:/Users/bernh/fizzbuzzDB/database.db

Apply migrations from directory migrations to a SQLite database:
-> yoyo apply --database sqlite:////C:/Users/bernh/fizzbuzzDB/database.db ./migrations

Create package "migrations" on repo
Add files to access the DB to this package.

