from flask import Flask, request, jsonify, abort
from models import setup_db, Courses, Student
from auth import AuthError, requires_auth
from flask_cors import CORS
import json


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resource={r'/api/*': {'origins': '*'}})

    def get_app():
        return app

    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Contect-Type, Autherization')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET, POST, PATCH, DELETE')
        return response

    # return list of students
    @app.route('/students')
    @requires_auth('get:students_details')
    def get_students(payload):
        students = Student.query.all()
        formatted_students = []
        for s in students:
            record = s.description()
            formatted_students.append(record)
        return jsonify({
            'success': True,
            'students': formatted_students})

    # take student information and add it
    @app.route('/students', methods=['POST'])
    @requires_auth('post:new_student')
    def insert_student(payload):
        Message_body = request.get_json()
        New_student = Student()
        if not Message_body:
            abort(400)
        name = Message_body.get('name', None)
        level = Message_body.get('level', None)
        if not name or not level:
            abort(400)
        New_student.name = name
        New_student.level = level
        New_student.insert()
        return jsonify({'success': True})

    # return list of courses
    @app.route('/courses')
    @requires_auth('get:courses_details')
    def get_courses(payload):
        courses = Courses.query.all()
        formatted_courses = []
        for c in courses:
            record = c.description()
            formatted_courses.append(record)
        return jsonify({
            'success': True,
            'courses': formatted_courses
        })

    # take course information and add it
    @app.route('/courses', methods=['POST'])
    @requires_auth('post:new_course')
    def insert_course(payload):
        Message_body = request.get_json()
        New_course = Courses()
        if not Message_body:
            abort(400)
        name = Message_body.get('name', None)
        courseTimePeriod = Message_body.get('courseTimePeriod', None)
        if not name or not courseTimePeriod:
            abort(400)
        New_course.name = name
        New_course.courseTimePeriod = courseTimePeriod
        New_course.insert()
        return jsonify({'success': True})

    # update specific course information
    @app.route('/courses/<int:id>', methods=['PATCH'])
    @requires_auth('patch:edit_course')
    def update_course(payload, id):
        course = Courses.query.get(id)
        if not course:
            abort(404)
        Message_body = request.get_json()
        course.name = Message_body.get('name')
        course.courseTimePeriod = Message_body.get('courseTimePeriod')
        course.update()
        courses = Courses.query.all()
        formatted_courses = []
        for c in courses:
            record = c.description()
            formatted_courses.append(record)
        return jsonify({
            'success': True,
            'courses': formatted_courses
        })

    # delete specific course
    @app.route('/courses/<int:id>', methods=['DELETE'])
    @requires_auth('delete:delete_course')
    def delete_course(payload, id):
        course = Courses.query.get(id)
        if not course:
            abort(404)
        course.delete()
        return jsonify({
            'success': True,
            'deleted': id
        })

    # Error Handling
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
            }), 422

    @app.errorhandler(404)
    def resourceNotFound(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
            }), 404

    @app.errorhandler(401)
    def notAuthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "not authorized to access API"
            }), 401

    @app.errorhandler(403)
    def notAuthorizedResource(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": "you do not have access to this resource"
            }), 403

    @app.errorhandler(400)
    def BadRequest(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request, you did not provide information"
            }), 400

    @app.errorhandler(AuthError)
    def handle_error(error):
        return jsonify({
            'success': False,
            'error': error.status_code,
            'message': error.error['description']
        }), error.status_code
    if __name__ == '__main__':
        app.run()

    return app
