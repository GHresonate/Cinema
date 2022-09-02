from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    username = models.CharField(max_length=256, unique=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    card_number = models.IntegerField(null=True)
    languishes = [
        ('UA', 'Ukrainian'),
        ('EN', 'English'),
        ('RU', 'Russian')
    ]
    language = models.CharField(max_length=2, choices=languishes)
    genders = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Different', 'Different'),
    ]
    gender = models.CharField(max_length=32, choices=genders)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManager()


class Ticket(models.Model):
    place = models.IntegerField()
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    session = models.ForeignKey('cinema_app.session', on_delete=models.CASCADE)
