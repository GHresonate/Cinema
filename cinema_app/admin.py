from django.contrib import admin
from .models import Cinema, Hall, Movie, Kontact, Session

admin.site.register((Cinema, Hall, Movie, Kontact, Session))
