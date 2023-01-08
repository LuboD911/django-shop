
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from bestshop.products.models import Product
from tests.base.tests import BestShopTestCase

UserModel = get_user_model()

class HomeTests(BestShopTestCase):

    def test_templateUsed(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')


    def test_getContextData(self):
        client = Client()
        response = client.get(reverse('home'))
        products = list(response.context['all_products'])
        self.assertEqual(200, response.status_code)
        self.assertListEqual(products, list(response.context['all_products']))
        self.assertListEmpty(products)




class ProductDetailsTest(BestShopTestCase):

    def test_getProductDetails_whenProductExistsAndIsOwner(self):
        self.client.force_login(self.user)
        product = Product.objects.create(
            title='Test Product',
            description='Test product description',
            price=123.60,
            image='path/to/image.png',
            user=self.user,
        )

        response = self.client.get(reverse('details product', kwargs={
            'pk': product.id,
        }))

        self.assertTrue(response.context['is_owner'])



