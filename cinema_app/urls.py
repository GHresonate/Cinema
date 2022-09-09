from django.urls import path
from . import views
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('movies', views.movies, name='front_movies'),
    path('schedule', views.schedule, name='front_schedule'),
    path('cinemas', views.cinemas, name='front_cinemas'),
    path('next_movies', views.next_movies, name='front_next_movies'),
    path('movie/<slug:url>', views.movie, name='front_movie'),
    path('cinema/<slug:url>', views.cinema, name='front_cinema'),
    path('hall/<slug:url>', views.hall, name='front_hall'),
    path('hall/<slug:url>/get_scheme', views.get_hall, name='front_get_hall')
]