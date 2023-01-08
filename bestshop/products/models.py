from django.contrib.auth import get_user_model
from django.db import models

from bestshop.validators.validators import validate_price, validate_rating

UserModel = get_user_model()

class Product(models.Model):
    title = models.CharField(
        max_length=25,
    )

    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[validate_price]
    )

    image = models.ImageField(
        default='image.png',
        upload_to='products',
        blank=True,

    )


    description = models.TextField(
        max_length=155,
    )

# тука правя да не е задължителна стойност за да мога да си направя тестовете без да създавам user
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

class Comment(models.Model):
    text = models.TextField(
        max_length=50,
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

class Ratings(models.Model):
    rating_price = models.IntegerField(
        validators=[validate_rating]
    )
    rating_quality = models.IntegerField(
        validators=[validate_rating]
    )
    rating_design = models.IntegerField(
        validators=[validate_rating]
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

class Purchase(models.Model):

    purchase_date = models.DateField()

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )