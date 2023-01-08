from django.core.exceptions import ValidationError
from django.test import TestCase

from bestshop.accounts.models import BestShopUser, Profile
from bestshop.products.models import Product
from django.contrib.auth.models import AnonymousUser, User
from django.contrib.auth import get_user_model

UserModel = get_user_model()
class TestProductObjectPrice(TestCase):

    title = "T-shirt"

    price = 100

    image = 'products/90_1001419-1A01052_1B000_10_MedusaHoodie-Sweatshirts-versace-online-store_0_0.webp'

    description = 'Very cool T-shirt'


    def test_whenPriceIsLessThan10_expectSomething(self):
        price = 2
        product = Product(title=self.title,price=price,image=self.image,
                          description=self.description)

        with self.assertRaises(ValidationError) as context:
            product.full_clean()
            product.save()

        self.assertIsNotNone(context.exception)


    def test_whenPriceIsBiggerThan999_expectSomething(self):
        price = 1000
        product = Product(title=self.title,price=price,image=self.image,
                          description=self.description)

        with self.assertRaises(ValidationError) as context:
            product.full_clean()
            product.save()

        self.assertIsNotNone(context.exception)

    def test_whenPriceIs100_expectNothing(self):
        price = 100
        product = Product(title=self.title, price=price, image=self.image,
                          description=self.description)
        product.full_clean()
        product.save()


    def test_whenPriceIsMoreThan100_expectNothing(self):
        price = 105
        product = Product(title=self.title, price=price, image=self.image,
                          description=self.description)
        product.full_clean()
        product.save()

    def test_whenTheModelDoesNotHaveAnImage_UseDefault_expectNothing(self):
        price = 100
        product = Product(title=self.title, price=price,
                          description=self.description)
        product.full_clean()
        product.save()

