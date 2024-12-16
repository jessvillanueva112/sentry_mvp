from flask import Blueprint, request, jsonify
from app.models import db, Student, RiskAssessment, SupportPlan

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([student.to_dict() for student in students])

@api_blueprint.route('/risk-assessment', methods=['POST'])
def add_risk_assessment():
    data = request.json
    new_assessment = RiskAssessment(**data)
    db.session.add(new_assessment)
    db.session.commit()
    return jsonify({"message": "Risk assessment added"}), 201

@api_blueprint.route('/support-plans', methods=['POST'])
def add_support_plan():
    data = request.json
    new_plan = SupportPlan(**data)
    db.session.add(new_plan)
    db.session.commit()
    return jsonify({"message": "Support plan added"}), 201