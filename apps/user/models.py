from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Model to store users
    """
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']
    USERNAME_FIELD = 'email'

    def __str__(self) -> str:
        return self.username
