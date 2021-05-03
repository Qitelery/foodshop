from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    middle_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=40)
    type_account = models.BooleanField(default=False)