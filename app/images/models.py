from django.contrib.auth.models import AbstractUser
from django.db import models
from versatileimagefield.fields import VersatileImageField, PPOIField


class CustomUser(AbstractUser):
    pass


class Account(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class User(models.Model):
    username = models.CharField(max_length=255)
    account_type = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.username}"


class Image(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    image = VersatileImageField("Image", upload_to="images/", ppoi_field="image_ppoi")
    image_ppoi = PPOIField()

    def __str__(self):
        return f"{self.user_id}"
