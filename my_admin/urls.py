from django.urls import path
from . import views
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('add_movie', views.add_movie, name='add_movie'),
    path('add_cinema', views.add_cinema, name='add_cinema'),
    path('add_page', views.add_page, name='add_page'),
    path('add_news', views.add_news, name='add_news'),
    path('add_disc', views.add_disc, name='add_discounts'),
    path('add_hall/<int:number>', views.add_hall, name='add_hall'),
    path('change_banners', views.change_banners, name='change_banners'),
    path('change_contacts', views.change_contacts, name='change_contacts'),
    path('change_changeNewsAndDiskInBanner', views.changeNewsAndDiskInBanner, name='change_changeNewsAndDiskInBanner'),
    path('change_main', views.change_main, name='change_main'),
    path('movies', views.movies, name='movies'),
    path('users', views.users, name='users'),
    path('pages', views.pages, name='pages'),
    path('cinemas', views.cinemas, name='cinemas'),
    path('news', views.news, name='news'),
    path('discounts', views.discounts, name='discounts'),
    path('movies/<slug:url>', views.change_movie, name='change_movie'),
    path('cinemas/<slug:url>', views.change_cinema, name='change_cinema'),
    path('pages/<slug:url>', views.change_page, name='change_page'),
    path('users/<slug:username>', views.change_user, name='change_user'),
    path('news/<slug:url>', views.change_news, name='change_news'),
    path('discounts/<slug:url>', views.change_discount, name='change_discount'),
]
