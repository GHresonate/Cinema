from django.contrib import admin
from .models import Gallery, Photo, SEO, Pages, MainPage, NewsAndDiscInBanner, NewsAndDiscount, BannersInTheTop, Background

admin.site.register((Gallery, Photo, SEO, Pages, MainPage, NewsAndDiscInBanner, NewsAndDiscount, BannersInTheTop, Background))
