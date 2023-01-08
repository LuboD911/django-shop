from django.core.exceptions import ValidationError
from django.test import TestCase

from bestshop.products.forms import ProductForm



class TestProductForm(TestCase):



    def test_whenTheForm_isValid_NoDots(self):

        data = {
            'title': 'T-shirt Blue',
            'price': 123.00,
            'description': 'Very very very cool T-shirt'
        }


        form = ProductForm(data)

        self.assertTrue(form.is_valid())


    def test_whenTreForm_isNotValid_WithDots(self):


        data = {
            'title': 'T.-shi.rt. Blue',
            'price': 131.05,
            'description': 'Very very very cool T-shirt'
        }
        form = ProductForm(data)
        with self.assertRaises(ValueError) as context:
            form.save()

        self.assertIsNotNone(context.exception)

