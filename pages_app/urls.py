from django.urls import path
from . import views

urlpatterns = [
    path('promotions', views.promotions, name='promotions'),
    path('promotion/<slug:url>', views.promotion, name='promotion'),
    path('news', views.news, name='front_news'),
    path('contacts', views.contacts, name='front_contacts'),
    path('app_prom', views.app_prom, name='front_app_prom'),
    path('food_court', views.food_court, name='front_food_court'),
    path('for_partners', views.for_partners, name='front_for_partners'),
    path('vip_hall', views.vip_hall, name='front_vip_hall'),
    path('children', views.children, name='front_children'),
    path('the_cinema', views.the_cinema, name='front_the_cinema'),
    path('a_news/<slug:url>', views.a_news, name='front_a_news'),
]
