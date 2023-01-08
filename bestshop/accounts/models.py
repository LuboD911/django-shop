from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from bestshop.accounts.managers import BestShopUserManager

class BestShopUser(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(
        unique=True,
        max_length=25,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'username'

    # нали редактира някви неща по мениджъра и не ти е default
    objects = BestShopUserManager()

class Profile(models.Model):
    profile_image = models.ImageField(
        upload_to='profiles',
        blank=True,
    )

    user = models.OneToOneField(
        BestShopUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

from .signals import *

