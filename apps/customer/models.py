from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Customer(models.Model):
    """
    Model to store customers
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"

