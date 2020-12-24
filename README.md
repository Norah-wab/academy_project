# awesome-academy API
## Project description
The awesome-academy system is used to store and keep track of students registration in different courses avaible in the system.
The users can view, add, delete and upadte courses and students based on autherty as followed :-
1- students access :
    * can view list of courses avaliable in the system. 
2- administrator users can: 
    * can view list of courses avaliable in the system. 
    * add new course in the awesome-academy system. 
    * update course in the awesome-academy system. 
    * delete course in the awesome-academy system. 
    * can view list of students avaliable in the system. 
    * add new student in the awesome-academy system. 
In this readme file you will find a description for each endpoint on how to use each one. 
## Getting stareted
### install dependencies 
#### python 
Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)
#### PIP Dependencies
run this command: pip install -r requirements.txt
This will install all of the required packages we selected within the `requirements.txt` file.
##### Key Dependencies
here is list of main dependencies
- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.
### Database Setup
With Postgres running create 2 databses for testing and production. 
1- academy: this is production db to create run this command createDB academy
2- academy_test: this is test db to create this is run this command createDB academy_test
### Running the server
To run the server go to folder you installed name: academy_project and run command line on this folder and follow these steps:
1- run this command to add all enviroment variables: . setup.sh
2- run this command to run the server: export FLASK_APP=app
                                       flask run --reload
### run ready to use unit test for the system
To run the test cases we write go the folder you installed name: academy_project and make sure that you run the server as descriped in 'Running the server' section of this file. After that, run command line on this folder and follow these steps:
1- run this command to add all enviroment variables: . setup.sh
2- run this command to run test file: python3 test.py
## project deployment access
This project avaliable on https://awesome-academy.herokuapp.com avaliable endpoint as following:-
1- get: https://awesome-academy.herokuapp.com/courses : used to get list of avaible courses.
2- get: https://awesome-academy.herokuapp.com/students : used to get list of avaible student.
3- delete: https://awesome-academy.herokuapp.com/courses/2 : used to delete specific course.
4- patch : https://awesome-academy.herokuapp.com/courses/2 : used to update specific course.
5- post: https://awesome-academy.herokuapp.com/courses : used to create new course. 
6- post: https://awesome-academy.herokuapp.com/students : used to create new student. 
In file academyTests.postman_collection.json you find sample of request and reponse and you can use postman to run the tests. 
## Error handling 
During using  awesome-academy API you may recieve one of these:
    * 404 –-> resource not found
    * 422 –-> unprocessable
    * 401 –-> not authorized to access API
    * 400 --> bad request
    * 403 -->  not authorized resource
