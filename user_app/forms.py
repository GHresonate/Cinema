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
    birthday = forms.DateField(localize=True, widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),)
    phone_number = forms.CharField(max_length=64)
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
        fields = ('username', 'email', 'name', 'surname', 'birthday', 'phone_number', 'address', 'card_number', 'language', 'gender')


class CustomUserChangeForm(forms.ModelForm):
    name = forms.CharField(max_length=256)
    surname = forms.CharField(max_length=256)
    username = forms.CharField(max_length=256)
    address = forms.CharField(max_length=256)
    birthday = forms.DateField(localize=True, widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),)
    phone_number = forms.CharField(max_length=64)
    card_number = forms.IntegerField()
    languishes = [
        ('UA', 'Українська'),
        ('EN', 'English'),
        ('RU', 'Руский')
    ]
    """attrs={"class":"form-select"})"""
    language = forms.ChoiceField(choices=languishes, widget=forms.Select(attrs={"class":"form-select"}))
    genders = [
        ('Male', 'Мужской'),
        ('Female', 'Женский'),
        ('Different', 'Другой'),
    ]
    gender = forms.ChoiceField(choices=genders, widget=forms.Select(attrs={"class":"form-select"}))

    class Meta:
        model = CustomUser
        fields = ('username', 'name', 'surname', 'address','birthday','phone_number', 'card_number', 'language', 'gender')

