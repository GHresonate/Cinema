from django.db import models


class Cinema(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    main_photo = models.ImageField()
    photo_list = models.OneToOneField('pages_app.Gallery', null=True, on_delete=models.SET_NULL)
    seo = models.OneToOneField('pages_app.SEO', null=True, on_delete=models.SET_NULL)


class Hall(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=128)
    created_date = models.DateField()
    description = models.TextField()
    scheme = models.JSONField()
    main_photo = models.ImageField()
    photo_list = models.OneToOneField('pages_app.Gallery', null=True, on_delete=models.SET_NULL)
    seo = models.OneToOneField('pages_app.SEO', null=True, on_delete=models.SET_NULL)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)


class Movie(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    main_photo = models.ImageField()
    photo_list = models.OneToOneField('pages_app.Gallery', null=True, on_delete=models.SET_NULL)
    seo = models.OneToOneField('pages_app.SEO', null=True, on_delete=models.SET_NULL)
    trailer_url = models.URLField()
    types = [
        ('2D', '2D'),
        ('3D', '3D'),
        ('IMAX', 'IMAX'),
    ]
    is_2D = models.BooleanField(default=False)
    is_3D = models.BooleanField(default=False)
    is_IMAX = models.BooleanField(default=False)


class Kontact(models.Model):
    name = models.CharField(max_length=256)
    address = models.TextField()
    coordinate = models.CharField(max_length=256)
    photo_list = models.OneToOneField('pages_app.Gallery', null=True, on_delete=models.SET_NULL)


class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    time = models.TimeField()
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.IntegerField()
    day = models.DateField()






