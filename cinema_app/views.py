from django.core.paginator import Paginator
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Movie
from pages_app.models import MainPage, Photo


def movies(request):
    movie = Movie.objects.all().order_by("-id")
    pagi = Paginator(movie, 15)
    page_number = request.GET.get('page')
    page = pagi.get_page(page_number)
    about_cinema = MainPage.objects.get(pk=1)
    return render(request, 'cinema_app/movies.html', {'page': page, "about_cinema": about_cinema})


def movie(request, url):
    movie = get_object_or_404(Movie, seo__url=url)
    about_cinema = MainPage.objects.get(pk=1)
    photos = Photo.objects.all().filter(id=movie.photo_list)
    return render(request, 'cinema_app/movie.html', {'movie': movie, "about_cinema": about_cinema})
