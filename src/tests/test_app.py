# Задача №1 unit-tests

import unittest
from unittest.mock import patch
import app


class AppTest(unittest.TestCase):
    def setUp(self):
        with open("/Users/user/PycharmProjects/src/fixtures/directories.json", 'r') as f:
            self.directories = f.read()
        with open("/Users/user/PycharmProjects/src/fixtures/documents.json", 'r') as f:
            self.documents = f.read()

    def test_get_info(self):
        self.assertIn("10006", self.documents)
        self.assertNotIn("111", self.documents)
        self.assertIsNotNone(self.documents)

    def test_add_new_doc(self):
        with patch('app.input', side_effect=[777, 'passport', 'David Hasselhoff', 4]):
            app.add_new_doc()

    def test_del_doc(self):
        with patch('app.input', side_effect="10006"):
            app.delete_doc()

    def test_remove_doc(self):
        with patch('app.input', side_effect="10006"):
            app.remove_doc_from_shelf("10006")


if __name__ == '__main__':
    unittest.main()
