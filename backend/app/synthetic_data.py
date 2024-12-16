import random

def generate_students(num_students=100):
    students = []
    for i in range(num_students):
        students.append({
            "id": i,
            "name": f"Student {i}",
            "age": random.randint(10, 18),
            "risk_level": random.choice(["Low", "Medium", "High"]),
            "violence_incidents": [random.randint(1, 10) for _ in range(random.randint(1, 5))],
            "counselor_notes": [f"Note {j}" for j in range(random.randint(1, 3))]
        })
    return students

def generate_counselors(num_counselors=10):
    counselors = []
    for i in range(num_counselors):
        counselors.append({
            "id": i,
            "specialization": random.choice(["Behavioral", "Academic", "Emotional"]),
            "assigned_students": random.sample(range(100), random.randint(5, 15))
        })
    return counselors

def generate_risk_assessments(students):
    assessments = []
    for student in students:
        assessments.append({
            "student_id": student["id"],
            "poverty_level": random.choice(["Low", "Medium", "High"]),
            "mental_health_issues": ["Anxiety", "Depression"][:random.randint(0, 2)],
            "behavioral_patterns": ["Aggression", "Bullying"][:random.randint(0, 2)],
            "risk_score": random.uniform(0, 1) * 100
        })
    return assessments

def generate_support_plans(students):
    support_plans = []
    for student in students:
        support_plans.append({
            "student_id": student["id"],
            "interventions": [f"Intervention {j}" for j in range(random.randint(1, 3))],
            "stakeholders": [f"Stakeholder {j}" for j in range(random.randint(1, 3))]
        })
    return support_plans

if __name__ == "__main__":
    students = generate_students()
    counselors = generate_counselors()
    assessments = generate_risk_assessments(students)
    support_plans = generate_support_plans(students)