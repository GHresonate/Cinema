from django import forms
from django_registration.forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(RegistrationForm):
    name = forms.CharField(max_length=256)
    surname = forms.CharField(max_length=256)
    username = forms.CharField(max_length=256)
    email = forms.EmailField()
    address = forms.CharField(max_length=256)
    card_number = forms.IntegerField()
    languishes = [
        ('UA', 'Ukrainian'),
        ('EN', 'English'),
        ('RU', 'Russian')
    ]
    language = forms.ChoiceField(choices=languishes)
    genders = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Different', 'Different'),
        ('Don`t say', 'Don`t say'),
    ]
    gender = forms.ChoiceField(choices=genders)

    class Meta(RegistrationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'name', 'surname', 'address', 'card_number', 'language', 'gender')


class CustomUserChangeForm(forms.ModelForm):
    name = forms.CharField(max_length=256)
    surname = forms.CharField(max_length=256)
    username = forms.CharField(max_length=256)
    address = forms.CharField(max_length=256)
    card_number = forms.IntegerField()
    languishes = [
        ('UA', 'Ukrainian'),
        ('EN', 'English'),
        ('RU', 'Russian')
    ]
    language = forms.ChoiceField(choices=languishes)
    genders = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Different', 'Different'),
        ('Don`t say', 'Don`t say'),
    ]
    gender = forms.ChoiceField(choices=genders)

    class Meta:
        model = CustomUser
        fields = ('username', 'name', 'surname', 'address', 'card_number', 'language', 'gender')