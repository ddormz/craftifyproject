


from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    rut = models.CharField('rut', max_length=10, unique=True)

    USERNAME_FIELD = "rut"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.rut