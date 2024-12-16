from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    risk_level = db.Column(db.String(50))
    violence_incidents = db.Column(db.JSON)
    counselor_notes = db.Column(db.JSON)

class Counselor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    specialization = db.Column(db.String(100))
    assigned_students = db.Column(db.JSON)

class RiskAssessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    poverty_level = db.Column(db.String(50))
    mental_health_issues = db.Column(db.JSON)
    behavioral_patterns = db.Column(db.JSON)
    risk_score = db.Column(db.Float)

class SupportPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    interventions = db.Column(db.JSON)
    stakeholders = db.Column(db.JSON)