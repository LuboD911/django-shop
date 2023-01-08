from django.core.exceptions import ValidationError
from django.test import TestCase

from bestshop.validators.validators import validate_dot_and_underscore


class ValidateDots(TestCase):

    def test_IfThereIs_aDot_expectToRaise(self):
        value = 'Name.Title.IDK'
        with self.assertRaises(ValidationError) as context:
            validate_dot_and_underscore(value)

        self.assertIsNotNone(context.exception)

    def test_ifThereIsNOT_aDot_expectNothing(self):
        value='Some random value'
        validate_dot_and_underscore(value)
