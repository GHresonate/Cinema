from django.core.paginator import Paginator
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Movie, Cinema, Hall, Session
from pages_app.models import MainPage, Photo, Pages, BannersInTheTop, Background, NewsAndDiscInBanner
from django.http import JsonResponse
import json
from datetime import date
from user_app.models import Ticket
from django.contrib.auth.decorators import login_required
from django.conf import settings
from datetime import datetime, timedelta
from django.utils import dateformat


def schedule(request):
    if request.method == 'GET':
        today = date.today()
        sessions = Session.objects.all().filter(date__gte=today).order_by('date', 'time')
        pagin = Paginator(sessions, 40)
        page_number = request.GET.get('page')
        page = pagin.get_page(page_number)
        about_cinema = MainPage.objects.all()[0]
        dates = []
        all_cinemas = Cinema.objects.all()
        all_dates = []
        all_movies = Movie.objects.all()
        all_halls = Hall.objects.all()
        today = date.today()
        for x in range(20):
            delta = timedelta(days=x)
            all_dates.append(today+delta)

        for session in page:
            if session.date not in dates:
                dates.append(session.date)
        return render(request, 'cinema_app/schedule.html',
                      {'page': page, 'dates': dates, "about_cinema": about_cinema, 'all_cinemas': all_cinemas,
                       'all_dates': all_dates, 'all_movies': all_movies, 'all_halls': all_halls})
    else:
        filters = json.load(request)
        print(filters)
        today = date.today()
        sessions = Session.objects.all().filter(date__gte=today).order_by('date', 'time')
        if 'is_2D' in filters:
            sessions = sessions.filter(movie__is_2D=True)
        if 'is_3D' in filters:
            sessions = sessions.filter(movie__is_3D=True)
        if 'is_IMAX' in filters:
            sessions = sessions.filter(movie__is_IMAX=True)
        if 'date' in filters:
            sessions = sessions.filter(date=filters['date'])
        if 'film' in filters:
            movie = Movie.objects.get(id=int(filters['film']))
            sessions = sessions.filter(movie=movie)
        if 'hall' in filters:
            hall = Hall.objects.get(id=int(filters['hall']))
            sessions = sessions.filter(hall=hall)
        if 'cinema' in filters:
            cinema = Cinema.objects.get(id=int(filters['cinema']))
            sessions = sessions.filter(cinema=cinema)


        pagin = Paginator(sessions, 40)
        page_number = request.GET.get('page')
        page = pagin.get_page(page_number)

        about_cinema = MainPage.objects.all()[0]
        dates = []
        all_cinemas = Cinema.objects.all()
        all_dates = []
        all_movies = Movie.objects.all()
        all_halls = Hall.objects.all()
        today = date.today()
        for x in range(20):
            delta = timedelta(days=x)
            all_dates.append(today+delta)

        for session in page:
            if session.date not in dates:
                dates.append(session.date)
        return render(request, 'cinema_app/schedule.html',
                      {'page': page, 'dates': dates, "about_cinema": about_cinema, 'all_cinemas': all_cinemas,
                       'all_dates': all_dates, 'all_movies': all_movies, 'all_halls': all_halls})


def main(request):
    today = date.today()
    top = BannersInTheTop.objects.all()
    top_first = top[0]
    top = top[1:]
    bottom = NewsAndDiscInBanner.objects.all()
    bottom_first = bottom[0]
    bottom = bottom[1:]
    formatted_date = today
    about_cinema = MainPage.objects.all()[0]
    today_movies = Session.objects.all().filter(date=today)
    following_films = Movie.objects.all().filter(realise_date__gt=today).order_by('realise_date')[:8]
    return render(request, 'cinema_app/index.html', {'about_cinema': about_cinema, 'top_first': top_first, 'top': top,
                                                     'bottom_first': bottom_first, 'bottom': bottom,
                                                     'today_movies': today_movies, 'following_films': following_films,
                                                     'formatted_date': formatted_date})


def movies(request):
    movie = Movie.objects.all().filter(realise_date__lte=datetime.now().date()).order_by("-id")
    pagi = Paginator(movie, 15)
    page_number = request.GET.get('page')
    page = pagi.get_page(page_number)
    about_cinema = MainPage.objects.all()[0]
    return render(request, 'cinema_app/movies.html', {'page': page, "about_cinema": about_cinema})


def cinemas(request):
    cinemas = Cinema.objects.all()
    pagin = Paginator(cinemas, 15)
    page_number = request.GET.get('page')
    page = pagin.get_page(page_number)
    the_cinema = Pages.objects.all().filter(name_ru="Главная страница")[0]
    about_cinema = MainPage.objects.all()[0]
    return render(request, 'cinema_app/cinemas.html',
                  {'page': page, "about_cinema": about_cinema, "the_cinema": the_cinema})


def next_movies(request):
    movies_next = Movie.objects.all().filter(realise_date__gt=datetime.now().date()).order_by("-id").order_by(
        '-realise_date')
    pagi = Paginator(movies_next, 15)
    page_number = request.GET.get('page')
    page = pagi.get_page(page_number)
    about_cinema = MainPage.objects.all()[0]
    return render(request, 'cinema_app/next_movies.html', {'page': page, "about_cinema": about_cinema})


def movie(request, url):
    the_movie = get_object_or_404(Movie, seo__url=url)
    about_cinema = MainPage.objects.get(pk=1)
    photos = Photo.objects.all().filter(gallery=the_movie.photo_list)
    sessions = Session.objects.all().filter(movie=the_movie).order_by('date', 'time')[:8]
    first_photo = photos[0]
    all_photos = photos[1:]
    return render(request, 'cinema_app/movie.html',
                  {'movie': the_movie, 'about_cinema': about_cinema, 'first_photo': first_photo,
                   'all_photos': all_photos, 'sessions': sessions})


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
    today = date.today()
    photos = Photo.objects.all().filter(gallery=the_hall.photo_list)
    sesssions_in_this_hall = Session.objects.all().filter(hall=the_hall).filter(date=today).order_by('date', 'time')
    first_photo = photos[0]
    all_photos = photos[1:]
    return render(request, 'cinema_app/hall.html',
                  {'hall': the_hall, "about_cinema": about_cinema, 'first_photo': first_photo,
                   'all_photos': all_photos, 'sesssions_in_this_hall': sesssions_in_this_hall})


def get_hall(request, url):
    the_hall = get_object_or_404(Hall, seo__url=url)
    return JsonResponse(the_hall.scheme, status=200)


def get_hall_for_booking(request, sc_id):
    session = get_object_or_404(Session, id=sc_id)
    the_hall = session.hall
    return JsonResponse(the_hall.scheme, status=200)


def get_price(request, sc_id):
    session = get_object_or_404(Session, id=sc_id)
    return JsonResponse({'price': session.price}, status=200)


def get_reserved(request, sc_id):
    session = Session.objects.get(id=sc_id)
    tickets = Ticket.objects.all().filter(session=session)
    result = {}
    for ticket in tickets:
        row = ticket.row
        if row not in result:
            result[row] = []
        result[row].append(ticket.place)
    json_result = json.dumps(result)
    return JsonResponse(json_result, status=200, safe=False)


@login_required
def booking(request, sc_id):
    session = get_object_or_404(Session, id=sc_id)
    movie = session.movie
    about_cinema = MainPage.objects.get(pk=1)
    return render(request, 'cinema_app/booking.html',
                  {'session': session, 'movie': movie, 'about_cinema': about_cinema})


@login_required
def ready(request, sc_id):
    ordered = json.load(request)
    session = Session.objects.get(id=sc_id)
    user = request.user
    for row in ordered:
        if ordered[row]:
            for place in ordered[row]:
                if place:
                    Ticket.objects.create(row=row, place=place, user=user, session=session)
    return get_reserved(request, sc_id)
