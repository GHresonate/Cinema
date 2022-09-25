from django.conf import settings
from django.core.paginator import Paginator
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import NewsAndDiscount, MainPage, Pages, Photo, Contact
from django.utils import translation
from cinema_app.models import Movie, Session





def contacts(request):
    conts = Contact.objects.all()
    about_cinema = MainPage.objects.get(pk=1)
    return render(request, 'pages_app/contacts.html', {'contacts': conts, 'about_cinema': about_cinema})


def app_prom(request):
    return render(request, 'pages_app/app_prom.html')


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
    anews = get_object_or_404(NewsAndDiscount, seo__url=url)
    about_cinema = MainPage.objects.get(pk=1)
    return render(request, 'pages_app/promotion.html', {'a_news': anews, "about_cinema": about_cinema})


def search(request):
    value = request.GET['search']
    movies = Movie.objects.all()
    about_cinema = MainPage.objects.get(pk=1)
    for movie in movies:
        if value in movie.name:
            photos = Photo.objects.all().filter(gallery=movie.photo_list)
            sessions = Session.objects.all().filter(movie=movie).order_by('date', 'time')[:8]
            first_photo = photos[0]
            all_photos = photos[1:]
            return render(request, 'cinema_app/movie.html',
                          {'movie': movie, 'about_cinema': about_cinema, 'first_photo': first_photo,
                           'all_photos': all_photos, 'sessions': sessions})
    return render(request, 'pages_app/Not_found.html',
                          {'movie': movie, 'about_cinema': about_cinema})



def get_page(request, url):
    page = Pages.objects.get(seo__url=url)
    photos = Photo.objects.all().filter(gallery=page.photo_list)
    about_cinema = MainPage.objects.get(pk=1)
    if url == 'Food_court':
        return render(request, 'pages_app/food_court.html',
                      {'page': page, "photos": photos, "about_cinema": about_cinema})
    return render(request, 'pages_app/page.html',
                  {'page': page, "photos": photos, "about_cinema": about_cinema})


