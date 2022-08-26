from django.core.paginator import Paginator
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Movie, Cinema
from pages_app.models import MainPage, Photo, Pages
from datetime import datetime


def movies(request):
    movie = Movie.objects.all().filter(realise_date__lte=datetime.now().date()).order_by("-id")
    pagi = Paginator(movie, 15)
    page_number = request.GET.get('page')
    page = pagi.get_page(page_number)
    about_cinema = MainPage.objects.get(pk=1)
    return render(request, 'cinema_app/movies.html', {'page': page, "about_cinema": about_cinema})


def cinemas(request):
    cinemas = Cinema.objects.all()
    pagi = Paginator(cinemas, 15)
    page_number = request.GET.get('page')
    page = pagi.get_page(page_number)
    the_cinema = Pages.objects.get(name="Main page")
    about_cinema = MainPage.objects.get(pk=1)
    return render(request, 'cinema_app/cinemas.html',
                  {'page': page, "about_cinema": about_cinema, "the_cinema": the_cinema})


def next_movies(request):
    movie = Movie.objects.all().filter(realise_date__gt=datetime.now().date()).order_by("-id").order_by('-realise_date')
    pagi = Paginator(movie, 15)
    page_number = request.GET.get('page')
    page = pagi.get_page(page_number)
    about_cinema = MainPage.objects.get(pk=1)
    return render(request, 'cinema_app/next_movies.html', {'page': page, "about_cinema": about_cinema})


def movie(request, url):
    movie = get_object_or_404(Movie, seo__url=url)
    about_cinema = MainPage.objects.get(pk=1)
    photos = Photo.objects.all().filter(gallery=movie.photo_list)
    first_photo = photos[0]
    all_photos = photos[1:]
    return render(request, 'cinema_app/movie.html',
                  {'movie': movie, "about_cinema": about_cinema, 'first_photo': first_photo, 'all_photos': all_photos})
