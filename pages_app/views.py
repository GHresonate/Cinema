from django.core.paginator import Paginator
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import NewsAndDiscount, MainPage, Pages


def promotions(request):
    proms = NewsAndDiscount.objects.all().filter(type='Discount', is_active=True).order_by("-date_published")
    pagi = Paginator(proms, 15)
    page_number = request.GET.get('page')
    page = pagi.get_page(page_number)
    about_cinema = MainPage.objects.get(pk=1)
    return render(request, 'pages_app/promotions.html', {'page': page, "about_cinema": about_cinema})


def promotion(request, url):
    prom = get_object_or_404(NewsAndDiscount, seo__url=url)
    about_cinema = MainPage.objects.get(pk=1)
    return render(request, 'pages_app/promotion.html', {'prom': prom, "about_cinema": about_cinema})


def news(request):
    news = NewsAndDiscount.objects.all().filter(type='News', is_active=True).order_by("-date_published")
    pagi = Paginator(news, 15)
    page_number = request.GET.get('page')
    page = pagi.get_page(page_number)
    about_cinema = MainPage.objects.get(pk=1)
    return render(request, 'pages_app/news.html', {'page': page, "about_cinema": about_cinema})


def a_news(request, url):
    prom = get_object_or_404(NewsAndDiscount, seo__url=url)
    about_cinema = MainPage.objects.get(pk=1)
    return render(request, 'pages_app/promotion.html', {'a_news': a_news, "about_cinema": about_cinema})
