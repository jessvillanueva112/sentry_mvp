import unittest
from app import create_app, db

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_students(self):
        response = self.client.get('/students')
        self.assertEqual(response.status_code, 200)

    def test_add_risk_assessment(self):
        response = self.client.post('/risk-assessment', json={
            'student_id': 1,
            'poverty_level': 'Medium',
            'mental_health_issues': ['Anxiety'],
            'behavioral_patterns': ['Aggression'],
            'risk_score': 75.0
        })
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()