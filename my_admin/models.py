from django.db import models


class Template(models.Model):
    file = models.FileField(unique=True)
    name = models.CharField(max_length=64, null=True)
