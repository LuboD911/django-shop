from django.core.exceptions import ValidationError
from django.test import TestCase

from bestshop.validators.validators import validate_price


class ValidatePrice(TestCase):

    def test_WhenPriceIsBiggerThan10_expectNothing(self):
        value = 150
        validate_price(value)

    def test_WhenPriceIs10_expectNothing(self):
        value = 10
        validate_price(value)

    def test_WhenPriceILessThan10_expectToRaise(self):
        value = 1
        with self.assertRaises(ValidationError) as context:
            validate_price(value)

        self.assertIsNotNone(context.exception)

