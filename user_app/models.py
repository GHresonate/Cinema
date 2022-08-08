from django.db import models

class User(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    nickname = models.CharField(max_length=256)
    email = models.EmailField()
    address = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    card_number = models.IntegerField
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
        ('Don`t say', 'Don`t say'),
    ]
    gender = models.CharField(max_length=32, choices=genders)
    phone_number = models.IntegerField()
    birthday = models.DateField()
    city = models.CharField(max_length=128)


class Ticket(models.Model):
    place = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    session = models.ForeignKey('cinema_app.session', on_delete=models.CASCADE)
