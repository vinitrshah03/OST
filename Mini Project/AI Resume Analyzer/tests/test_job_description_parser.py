import unittest
from models.job_description_parser import parse_job_description

class TestJobDescriptionParser(unittest.TestCase):
    def test_parse_job_description(self):
        doc = parse_job_description(
            "Looking for a Software Engineer with experience in Python and Java.",
            "Develop and deploy software systems.",
            "3+ years in backend development.",
            "Python, Java, SQL",
            "Bachelor's in Computer Science"
        )

        self.assertIsNotNone(doc)
        self.assertIn('keywords', doc)
        self.assertIsInstance(doc['keywords'], set)
        self.assertGreater(len(doc['keywords']), 0)

if __name__ == '__main__':
    unittest.main()
