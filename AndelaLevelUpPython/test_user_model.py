import unittest
from user_model import *


class TestUserModel(unittest.TestCase):

    # def setUp(self)
    def test_model_is_created(self):
        user = User('Barnabas', 'Tumu', '779100043', 'barna@gmail.com', '1234')

    def test_returns_valid_email(self):
        user = User('Barnabas', 'Tumu', '779100043', 'barna@gmail.com', '1234')
        self.assertEqual(user.validate_email(), 'barna@gmail.com')

    def test_returns_invalid_email(self):
        user = User('Barnabas', 'Tumu', '779100043', 'barna.com', '1234')
        self.assertEqual(user.validate_email(), 'Invalid email address!')

    def test_does_not_combine_non_alphabet_names(self):
        user = User('12345', 'Tumu', '779100043', 'barna@gmail.com', '1234')
        self.assertEqual(user.combine_name(), 'Names must be alphabets')

    def test_combines_alphabet_names(self):
        user = User('Barnabas', 'Tumu', '779100043', 'barna@gmail.com', '1234')
        self.assertEqual(user.combine_name(), 'Barnabas Tumu')

    def test_does_not_combine_non_alphabet_mixed_with_number_names(self):
        user = User('Barn1234', 'Tumu', '779100043', 'barna@gmail.com', '1234')
        self.assertEqual(user.combine_name(), 'Names must be alphabets')

    def test_validate_password_length(self):
        user = User('Barna', 'Tumu', '779100043', 'barna@gmail.com', 'Ba#@1')
        self.assertEqual(user.validate_password(), 'Password should be at least six characters long')

    def test_validate_characters_in_password(self):
        user = User('Barnabas', 'Tumu', '779100043', 'barna@gmail.com', 'Ba#@1234')
        self.assertEqual(user.validate_password(), 'Valid password!')
