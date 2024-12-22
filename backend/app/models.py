from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    violence_incidents = db.Column(db.PickleType, nullable=True)  # List of numbers
    counselor_notes = db.Column(db.PickleType, nullable=True)  # List of text

class Counselor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    specialization = db.Column(db.String(255), nullable=False)
    assigned_students = db.relationship('Student', backref='counselor', lazy=True)

class SupportPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    interventions = db.Column(db.PickleType, nullable=True)  # List of text
    stakeholders = db.Column(db.PickleType, nullable=True)  # List of text

class RiskAssessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    poverty_level = db.Column(db.String(255), nullable=True)
    mental_health_issues = db.Column(db.PickleType, nullable=True)  # List of text
    behavioral_patterns = db.Column(db.PickleType, nullable=True)  # List of text