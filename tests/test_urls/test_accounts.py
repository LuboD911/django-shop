
from django.urls import reverse,resolve
from django.test import SimpleTestCase

from bestshop.accounts.views import SignInView, logout_user, SignUpView, profile_details

class TestAccountsUrls(SimpleTestCase):


    def test_Logout_url(self):
        url = reverse('log out user')
        self.assertEquals(resolve(url).func, logout_user)


    def test_ProfileDetails_url(self):
        url = reverse('profile details')
        self.assertEquals(resolve(url).func, profile_details)