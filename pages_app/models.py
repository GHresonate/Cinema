from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Gallery(models.Model):
    pass


class Photo(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    photo = models.ImageField(null=True)


class SEO(models.Model):
    url = models.CharField(unique=True, max_length=128, null=True)
    title = models.CharField(max_length=128)
    keywords = models.TextField()
    definition = models.TextField()


class Pages(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    main_photo = models.ImageField()
    photo_list = models.OneToOneField(Gallery, null=True, on_delete=models.SET_NULL)
    seo = models.OneToOneField(SEO, null=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField(default=True)


class MainPage(models.Model):
    phone_number = PhoneNumberField()
    phone_number2 = PhoneNumberField()
    seo_text = models.TextField()
    seo = models.OneToOneField(SEO, null=True, on_delete=models.SET_NULL)


class BannersInTheTop(models.Model):
    main_photo = models.ImageField()
    text = models.TextField()
    url = models.CharField(max_length=256)


class Background(models.Model):
    main_photo = models.ImageField(null=True, blank=True)
    is_photo = models.BooleanField(default=True)
    color = models.CharField(max_length=32, null=True, blank=True)


class NewsAndDiscInBanner(models.Model):
    main_photo = models.ImageField()
    trailer_url = models.CharField(max_length=64)


class NewsAndDiscount(models.Model):
    types = [
        ('News', 'News'),
        ('Discount', 'Discount')
    ]
    type = models.CharField(max_length=16, choices=types, null=True)
    date_published = models.DateField(null=True)
    description = models.TextField()
    name = models.CharField(max_length=256)
    main_photo = models.ImageField()
    photo_list = models.OneToOneField(Gallery, null=True, on_delete=models.SET_NULL)
    trailer_url = models.URLField(null=True)
    seo = models.OneToOneField(SEO, null=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField(default=False)


class Contact(models.Model):
    name = models.CharField(max_length=256)
    address = models.TextField()
    coordinate = models.TextField()
    main_photo = models.ImageField()
