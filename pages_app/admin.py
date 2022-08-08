from django.contrib import admin
from .models import Gallery, Photo, SEO, Pages, MainPage, Banners, NewsAndDiscInBanner, NewsAndDiscont

admin.site.register((Gallery, Photo, SEO, Pages, MainPage, Banners, NewsAndDiscInBanner, NewsAndDiscont))
