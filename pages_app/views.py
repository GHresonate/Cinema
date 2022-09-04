from django.conf import settings
from django.core.paginator import Paginator
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import NewsAndDiscount, MainPage, Pages, Photo, Contact
from django.utils import translation


def children(request):
    child = Pages.objects.get(name="Children room")
    photos = Photo.objects.all().filter(gallery=child.photo_list)
    about_cinema = MainPage.objects.get(pk=1)
    return render(request, 'pages_app/children.html',
                  {'children': child, "photos": photos, "about_cinema": about_cinema})


def vip_hall(request):
    viphall = Pages.objects.get(name="Vip hall")
    photos = Photo.objects.all().filter(gallery=viphall.photo_list)
    about_cinema = MainPage.objects.get(pk=1)
    return render(request, 'pages_app/vip_hall.html',
                  {'vip_hall': viphall, "photos": photos, "about_cinema": about_cinema})


def for_partners(request):
    for_par = Pages.objects.get(name="For partners")
    photos = Photo.objects.all().filter(gallery=for_par.photo_list)
    about_cinema = MainPage.objects.get(pk=1)
    return render(request, 'pages_app/for_partnes.html',
                  {'for_par': for_par, "photos": photos, "about_cinema": about_cinema})


def the_cinema(request):
    the_cinema = Pages.objects.get(name="Main page")
    photos = Photo.objects.all().filter(gallery=the_cinema.photo_list)
    about_cinema = MainPage.objects.get(pk=1)
    return render(request, 'pages_app/the_cinema.html',
                  {'the_cinema': the_cinema, "photos": photos, "about_cinema": about_cinema})


def contacts(request):
    conts = Contact.objects.all()
    about_cinema = MainPage.objects.get(pk=1)
    return render(request, 'pages_app/contacts.html', {'contacts': conts, 'about_cinema': about_cinema})


def food_court(request):
    food = Pages.objects.get(name="Food court")
    photos = Photo.objects.all().filter(gallery=food.photo_list)
    about_cinema = MainPage.objects.get(pk=1)
    return render(request, 'pages_app/food_court.html', {'food': food, "photos": photos, "about_cinema": about_cinema})


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


