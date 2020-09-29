from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from project import settings


class User(AbstractUser):
    full_name = models.CharField(max_length=300, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to='pics', blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    is_premium = models.BooleanField(null=True, blank=True)

