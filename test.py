import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from models import setup_db, create_DB, Courses
from flask_cors import CORS
from auth import AuthError, requires_auth
from app import create_app


class academy(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "academy_test"
        self.database_path = "postgresql://@{}/{}".format(
            'localhost:5432', self.database_name)
        self.studentToken = os.environ.get('student')
        self.administratorToken = os.environ.get('administrator')
        # binds the app to the current context
        with self.app.app_context():
            setup_db(self.app, self.database_path)
            # create all tables
            create_DB()

    def tearDown(self):
        """Executed after reach test"""
        pass

    # get list of avalible courses on the system
    def test_get_courses(self):
        headers = {"authorization": "Bearer " + self.studentToken}
        response = self.client().get('/courses', headers=headers)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    # create new course in the system
    def test_create_courses(self):
        headers = {"authorization": "Bearer " + self.administratorToken}
        response = self.client().post('/courses', headers=headers, json={
            "name": "computer sicinse",
            "courseTimePeriod": "Night"})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    # update existing course in the system
    def test_update_courses(self):
        headers = {"authorization": "Bearer " + self.administratorToken}
        response = self.client().patch('/courses/1', headers=headers, json={
            "name": "computer science",
            "courseTimePeriod": "Morning"})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    # delete existing course from the system
    def test_delete_course(self):
        headers = {"authorization": "Bearer " + self.administratorToken}
        course = Courses(
            name="data visulization",
            courseTimePeriod="morning")
        course.insert()
        id = course.id
        response = self.client().delete(
            '/courses/{}'.format(id), headers=headers)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    # get list avalible students on the system
    def test_get_students(self):
        headers = {"authorization": "Bearer " + self.administratorToken}
        response = self.client().get('/students', headers=headers)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    # create new student
    def test_create_student(self):
        headers = {"authorization": "Bearer " + self.administratorToken}
        response = self.client().post('/students', headers=headers, json={
            "name": "Abdullah",
            "level": "elementary"})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    # create course Not authorize
    def test_create_courses_not_authorized(self):
        response = self.client().post('/courses', json={
            "name": "computer sicinse",
            "courseTimePeriod": "Night"})
        self.assertEqual(response.status_code, 401)

    # delete course not exist in the system
    def test_delete_course_not_exist(self):
        headers = {"authorization": "Bearer " + self.administratorToken}
        response = self.client().delete('/courses/200', headers=headers)
        self.assertEqual(response.status_code, 404)

    # try to get course list with expired token
    def test_getCourseList_TokenNotValid(self):
        expiredToken = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjB6alRIQ0c1a05IRHNXMWg5eEJwdCJ9.eyJpc3MiOiJodHRwczovL2ZzbmRub3JhaC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY5YTU3YWE3NWIyZjYwMDY5YWNiMGRlIiwiYXVkIjoiYWNhZGVteSIsImlhdCI6MTYwNzkzNzQ5OCwiZXhwIjoxNjA3OTQ0Njk4LCJhenAiOiJOc1FCd1VtQllvTDgyNDRhUmpib3lxMkQ1UHB0S2k0MiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmNvdXJzZXNfZGV0YWlscyJdfQ.jq3hzn1800XdhRNwLTfITrIKAPSe7V2jmKKa8GDYW7roPka-V1da765YfWOpwr663jYCYreWKMIoP1KTHcK6Lbmr0y744ylex97KYRy0eeJTOm4v4418vB1iY3pUYx9XpcOuGwQx-lXUCbmo-x5p35Zjbt9_qToru-2oHcZ67uCaATXDR8TdLc2ahCXGi-rPeaFrTpFYVgZbnkHqgx12D3qG9UkhEV5qa7RCHH0s9TMcWnwBL-ue440Uqu6MVqTFg4CQ7LYf2IkvC1ag1EjLxqfBrMA_CyWdulr5UWnWF6JiBzRvnBM5iIvqFs92cTVuCHFL8mKdft08UmwEp8sGZg'
        headers = {"authorization": "Bearer " + expiredToken}
        response = self.client().get('/courses', headers=headers)
        self.assertEqual(response.status_code, 401)


if __name__ == "__main__":
    unittest.main()
