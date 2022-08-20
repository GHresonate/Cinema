from django.urls import path
from . import views

urlpatterns = [
    path('add_movie', views.add_movie, name='add_movie'),
    path('add_cinema', views.add_cinema, name='add_cinema'),
    path('add_page', views.add_page, name='add_page'),
    path('add_news', views.add_news, name='add_news'),
    path('movies', views.movies, name='movies'),
    path('pages', views.pages, name='pages'),
    path('cinemas', views.cinemas, name='cinemas'),
    path('movies/<slug:url>', views.change_movie, name='change_movie'),
]
