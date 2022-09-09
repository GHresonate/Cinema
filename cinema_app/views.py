from django.core.paginator import Paginator
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Movie, Cinema, Hall, Session
from pages_app.models import MainPage, Photo, Pages
from datetime import datetime
from django.http import JsonResponse
import json
from datetime import date

def schedule(request):
    today = date.today()
    sessions = Session.objects.all().filter(movie__realise_date__gte=today)
    pagin = Paginator(sessions, 40)
    page_number = request.GET.get('page')
    page = pagin.get_page(page_number)
    about_cinema = MainPage.objects.get(pk=1)
    return render(request, 'cinema_app/schedule.html', {'page': page, "about_cinema": about_cinema})

def movies(request):
    movie = Movie.objects.all().filter(realise_date__lte=datetime.now().date()).order_by("-id")
    pagi = Paginator(movie, 15)
    page_number = request.GET.get('page')
    page = pagi.get_page(page_number)
    about_cinema = MainPage.objects.get(pk=1)
    return render(request, 'cinema_app/movies.html', {'page': page, "about_cinema": about_cinema})


def cinemas(request):
    cinemas = Cinema.objects.all()
    pagin = Paginator(cinemas, 15)
    page_number = request.GET.get('page')
    page = pagin.get_page(page_number)
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


def cinema(request, url):
    cinema = get_object_or_404(Cinema, seo__url=url)
    about_cinema = MainPage.objects.get(pk=1)
    photos = Photo.objects.all().filter(gallery=cinema.photo_list)
    first_photo = photos[0]
    all_photos = photos[1:]
    halls = Hall.objects.all().filter(cinema=cinema)
    return render(request, 'cinema_app/cinema.html',
                  {'cinema': cinema, "about_cinema": about_cinema, 'first_photo': first_photo, 'all_photos': all_photos,
                   'halls': halls})


def hall(request, url):
    the_hall = get_object_or_404(Hall, seo__url=url)
    about_cinema = MainPage.objects.get(pk=1)
    photos = Photo.objects.all().filter(gallery=the_hall.photo_list)
    first_photo = photos[0]
    all_photos = photos[1:]
    return render(request, 'cinema_app/hall.html',
                  {'hall': the_hall, "about_cinema": about_cinema, 'first_photo': first_photo,
                   'all_photos': all_photos})


def get_hall(request, url):
    the_hall = get_object_or_404(Hall, seo__url=url)
    print(the_hall.scheme)
    return JsonResponse(the_hall.scheme, status=200)
