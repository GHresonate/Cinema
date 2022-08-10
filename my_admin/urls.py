from django.urls import path

from . import views

urlpatterns = [
    path('movie', views.set_movie, name='movie'),
    path('', views.main, name='main'),
]
