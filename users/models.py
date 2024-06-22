from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(null=True, blank=True)
    username = models.CharField(max_length=150)
    USERNAME_FIELD = 'phone_number'
    EMAIL_FIELD = 'id'
    father_name = models.CharField(max_length=150)
    birth_date = models.DateField(null=True, blank=True)
    province = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=150, unique=True)
    user_type = models.CharField(max_length=150, default="O'quvchi")

    def __str__(self):
        return str(self.id)