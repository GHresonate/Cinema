from django.urls import path
from . import views

urlpatterns = [
    path('movies', views.movies, name='front_movies'),
    path('cinemas', views.cinemas, name='front_cinemas'),
    path('next_movies', views.next_movies, name='front_next_movies'),
    path('movie/<slug:url>', views.movie, name='front_movie'),
]