from django.db import models


class Gallery(models.Model):
    pass


class Photo(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    photo = models.ImageField(null=True)


class SEO(models.Model):
    url = models.CharField(unique=True, max_length=128)
    title = models.CharField(max_length=128)
    keywords = models.TextField()
    description = models.TextField()




class Pages(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    main_photo = models.ImageField()
    photo_list = models.OneToOneField(Gallery, null=True, on_delete=models.SET_NULL)
    seo = models.OneToOneField(SEO, null=True, on_delete=models.SET_NULL)


class MainPage(models.Model):
    phone_number = models.IntegerField
    seo_text = models.TextField()
    seo = models.OneToOneField(SEO, null=True, on_delete=models.SET_NULL)


class Banners(models.Model):
    main_photo = models.ImageField()
    top_in_main = models.OneToOneField(Gallery, null=True, on_delete=models.SET_NULL)


class NewsAndDiscInBanner(models.Model):
    types = [
        ('News', 'News'),
        ('Discont', 'Discont')
    ]
    type = models.CharField(max_length=16, choices=types)
    main_photo = models.ImageField()
    url = models.URLField()
    text = models.TextField()
    page = models.ForeignKey(Banners, on_delete=models.CASCADE)


class NewsAndDiscont(models.Model):
    types = [
        ('News', 'News'),
        ('Discont', 'Discont')
    ]
    type = models.CharField(max_length=16, choices=types)
    date_published = models.DateField()
    description = models.TextField()
    name = models.CharField(max_length=256)
    main_photo = models.ImageField()
    photo_list = models.OneToOneField(Gallery, null=True, on_delete=models.SET_NULL)
    url = models.URLField()
    seo = models.OneToOneField(SEO, null=True, on_delete=models.SET_NULL)
