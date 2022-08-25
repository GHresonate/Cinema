from django.urls import path
from . import views

urlpatterns = [
    path('movies', views.movies, name='front_movies'),
    path('movie/<slug:url>', views.movie, name='front_movie'),
]