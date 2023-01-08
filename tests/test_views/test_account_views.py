import os
import random
from os.path import join
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from bestshop.accounts.models import Profile
from bestshop.products.models import Product
from tests.base.tests import BestShopTestCase


class ProfileDetailsTest(BestShopTestCase):
    def test_getDetails_whenLoggedInUserWithNoProducts_shouldGetDetailsWithNoProducts(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('profile details'))

        self.assertListEmpty(list(response.context['products']))
        self.assertEqual(self.user.id, response.context['profile'].user_id)

    def test_getDetails_whenLoggedInUserWithProducts_shouldGetDetailsWithProducts(self):
        product = Product.objects.create(
            title='Test Product',
            description='Test product description',
            price=123.60,
            image='path/to/image.png',
            user=self.user,
        )

        self.client.force_login(self.user)

        response = self.client.get(reverse('profile details'))

        self.assertEqual(200, response.status_code)
        self.assertEqual(self.user.id, response.context['profile'].user_id)
        self.assertListEqual([product], list(response.context['products']))

    def test_postDetails_whenUserLoggedInWithoutImage_shouldChangeImage(self):

        path_to_image = join(settings.BASE_DIR, 'tests', 'media', 'test_image.webp')

        file_name = f'{random.randint(1, 10000)}-test_image.webp'
        file = SimpleUploadedFile(
            name=file_name,
            content=open(path_to_image, 'rb').read(),
            content_type='image/jpeg')

        self.client.force_login(self.user)

        response = self.client.post(reverse('profile details'), data={
            'profile_image': file,
        })

        self.assertEqual(302, response.status_code)

        profile = Profile.objects.get(pk=self.user.id)
        self.assertTrue(str(profile.profile_image).endswith(file_name))

        path_to_remove = join(settings.BASE_DIR, 'media', 'profiles', file_name)

        os.remove(path_to_remove)

    def test_postDetails_whenUserLoggedInWithImage_shouldChangeImage(self):
        path_to_image = 'path/to/image.png'
        profile = Profile.objects.get(pk=self.user.id)
        profile.profile_image = path_to_image + 'old'
        profile.save()

        self.client.force_login(self.user)

        response = self.client.post(reverse('profile details'), data={
            'profile_image': path_to_image,
        })

        self.assertEqual(302, response.status_code)

        profile = Profile.objects.get(pk=self.user.id)

