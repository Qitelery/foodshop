from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), blank=True, null=True, max_length=30)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30)
    middle_name = models.CharField(_('middle name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    adress = models.CharField(_('adress'), max_length=256)
    phone = models.CharField(_('phone'), blank=True, null=True, max_length=32)
    pass_user = models.CharField(_('password'), blank=True, null=True, max_length=16)
    type_account = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def is_staff(self):
        # Simplest possible answer: All admins are staff
        return self.is_admin
