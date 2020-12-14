# Project description
This project is an awesome-academy where end users can view, add,delete and upadte courses and students based on autherty as followed :-
1- students access :
    * can view list of courses avaliable in the system. 
2- administrator users can: 
    * can view list of courses avaliable in the system. 
    * add new course in the awesome-academy system. 
    * update course in the awesome-academy system. 
    * delete course in the awesome-academy system. 
    * can view list of students avaliable in the system. 
    * add new student in the awesome-academy system. 
# project access
This project avaliable on https://awesome-academy.herokuapp.com avaliable endpoint as following:-
1- get: https://awesome-academy.herokuapp.com/courses : used to get list of avaible courses.
2- get: https://awesome-academy.herokuapp.com/students : used to get list of avaible student.
3- delete: https://awesome-academy.herokuapp.com/courses/2 : used to delete specific course.
4- patch : https://awesome-academy.herokuapp.com/courses/2 : used to update specific course.
5- post: https://awesome-academy.herokuapp.com/courses : used to create new course. 
6- post: https://awesome-academy.herokuapp.com/students : used to create new student. 
Note: there is unit testing included to get the needed tempary access for testing purpose file name:academyTests.postman_collection.json. 
# Error handling 
During using  awesome-academy API you may recieve one of these:
    * 404 –-> resource not found
    * 422 –-> unprocessable
    * 401 –-> not authorized to access API
    * 400 --> bad request
    * 403 -->  not authorized resource
