import unittest
from app.synthetic_data import generate_students, generate_risk_assessments

class SyntheticDataTestCase(unittest.TestCase):
    def test_generate_students(self):
        students = generate_students(10)
        self.assertEqual(len(students), 10)
        self.assertIn('name', students[0])

    def test_generate_risk_assessments(self):
        students = generate_students(10)
        assessments = generate_risk_assessments(students)
        self.assertEqual(len(assessments), 10)
        self.assertIn('risk_score', assessments[0])

if __name__ == '__main__':
    unittest.main()