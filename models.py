from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()

def setup_db(app):
    app.config.from_envvar('app_setting')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ.get('Trak_Modification')
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)

class Courses(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    courseTimePeriod = db.Column(db.String(), nullable=False)
    registered_courses = db.relationship('student_in_course', backref=db.backref('student', lazy=True), cascade="all, delete")
    def insert(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def description(self):
        return {
            'id': self.id,
            'name': self.name,
            'courseTimePeriod': self.courseTimePeriod
        }
class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    level = db.Column(db.String(), nullable=False)
    registered_courses = db.relationship('student_in_course', backref=db.backref('courses', lazy=True), cascade="all, delete")
    def insert(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def update(self):
        db.session.commit()
    def description(self):
        return {
            'id': self.id,
            'name': self.name,
            'level': self.level
        }
class student_in_course(db.Model):
    __tablename__ = 'student_in_course'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer,db.ForeignKey('students.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    def register_in_course(self):
        db.session.add(self)
        db.session.commit()