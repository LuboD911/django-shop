from django.urls import reverse, resolve
from django.test import SimpleTestCase

from bestshop.products.views import home, product_add, product_details,buy, product_delete,product_edit,comment_product



class TestProductUrls(SimpleTestCase):

    def test_Home_url(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_AddProduct_url(self):
        url = reverse('add product')
        self.assertEquals(resolve(url).func, product_add)

    def test_getProductDetails_url_resolves(self):
        url = reverse('details product', args=[1])
        self.assertEquals(resolve(url).func, product_details)

    def test_BuyProduct_url_resolves(self):
        url = reverse('buy', args=[1])
        self.assertEquals(resolve(url).func, buy)

    def test_ProductDelete_url_resolves(self):
        url = reverse('delete product', args=[1])
        self.assertEquals(resolve(url).func, product_delete)

    def test_ProductEdit_url_resolves(self):
        url = reverse('edit product', args=[1])
        self.assertEquals(resolve(url).func, product_edit)

    def test_ProductComment_url_resolves(self):
        url = reverse('comment product', args=[1])
        self.assertEquals(resolve(url).func, comment_product)
