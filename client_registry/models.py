from enum import unique
from django.db import models
# from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, AbstractUser
)


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # a admin user; non super-user
    is_admin = models.BooleanField(default=False) # a superuser
    username = models.CharField(max_length=254, null=False, unique=True)
    first_name = models.CharField(max_length=254, null=False, unique=False)
    last_name = models.CharField(max_length=254, null=False, unique=False)
    password = models.CharField(max_length=254, null=False)
    facility_code=models.CharField(max_length=254, null=False)

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    # def get_email(self):
    #     # The user is identified by their email address
    #     return self.email

    # def get_short_name(self):
    #     # The user is identified by their email address
    #     return self.email

    # def __str__(self):
    #     return self.email

    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     return self.staff

    # @property
    # def is_admin(self):
    #     "Is the user a admin member?"
    #     return self.admin