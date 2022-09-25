from django.urls import path, include
from . import views
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('promotions', views.promotions, name='promotions'),
    path('search', views.search, name='search'),
    path('page/<slug:url>', views.get_page, name='page'),
    path('promotion/<slug:url>', views.promotion, name='promotion'),
    path('news', views.news, name='front_news'),
    path('contacts', views.contacts, name='front_contacts'),
    path('app_prom', views.app_prom, name='front_app_prom'),
    path('a_news/<slug:url>', views.a_news, name='front_a_news'),
 #   path('change_lang/<slug:code>', views.select_lang, name='front_change_lang'),
]
