import os
import tempfile
import unittest

from src.employee import from_csv_file

SAMPLE_CSV = """name,age,job,salary
Alice,25,Engineer,50000
Bob,30,Analyst,60000
Jane,35,Manager,80000
John,40,CEO,100000
"""


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            mode="w",
            newline="",
            suffix=".csv",
        )
        cls.temp_file_name = cls.temp_file.name
        cls.temp_file.write(SAMPLE_CSV)
        cls.temp_file.close()
        cls.employees = from_csv_file(cls.temp_file_name)

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.temp_file_name)

    def test_total_employees(self):
        self.assertEqual(len(self.employees), 4)


if __name__ == "__main__":
    unittest.main()
