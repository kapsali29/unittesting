import unittest
import pandas as pd
from unittest.mock import MagicMock, patch

from src.employees import load_csv, calculate_len

class TestDF(unittest.TestCase):
    @staticmethod
    def static_employees() -> pd.DataFrame:
        employees_str = """
        name,age,job,salary
        Alice,25,Engineer,50000
        Bob,30,Analyst,60000
        Jane,35,Manager,80000
        John,40,CEO,100000
        """
        rows = employees_str.strip().split('\n')
        cols = rows[0].split(',')
        data = [row.strip().split(",") for row in rows[1:]]
        return pd.DataFrame(data=data, columns=cols)

    @patch('src.employees.load_csv')
    def test_employees_patch(self, mock_load_csv):
        mock_load_csv.return_value = self.static_employees()
        df = mock_load_csv.return_value
        self.assertEqual(
            calculate_len(df), 4
        )

    def test_employess_magic(self):
        load_csv = MagicMock()
        load_csv.return_value = self.static_employees()
        df = load_csv.return_value
        self.assertEqual(calculate_len(df), 4)


if __name__ == '__main__':
    unittest.main()
