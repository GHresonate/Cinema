from django.urls import path
from . import views

urlpatterns = [
    path('promotions', views.promotions, name='promotions'),
    path('promotion/<slug:url>', views.promotion, name='promotion'),
    path('news', views.news, name='front_news'),
    path('a_news/<slug:url>', views.a_news, name='front_a_news'),
]

