import unittest
from unittest.mock import MagicMock, patch
from src import unique_names


class TestUniqueNames(unittest.TestCase):
    def test_names(self):
        unique_names.get_names_from_file = MagicMock()
        unique_names.get_names_from_file.return_value = ["Panos", "Vas", "Ellie"]
        names = unique_names.get_unique_names("names.txt")
        self.assertListEqual(names, ['Ellie', 'Panos', 'Vas'])
    @patch('src.unique_names.get_names_from_file')
    def test_names_patch(self, mock_get_names_from_file):
        mock_get_names_from_file.return_value = ["Panos", "Vas", "Ellie"]
        names = unique_names.get_unique_names("names.txt")
        self.assertListEqual(names, ['Ellie', 'Panos', 'Vas'])

if __name__ == '__main__':
    unittest.main()
