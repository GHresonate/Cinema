from django.db import models


class Template(models.Model):
    file = models.FileField()
