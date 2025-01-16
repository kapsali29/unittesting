import unittest
from unittest.mock import MagicMock
from src import unique_names


class TestUniqueNames(unittest.TestCase):
    def test_names(self):
        unique_names.get_names_from_file = MagicMock()
        unique_names.get_names_from_file.return_value = ["Panos", "Vas", "Ellie"]
        names = unique_names.get_unique_names("names.txt")
        self.assertListEqual(names, ['Ellie', 'Panos', 'Vas'])
