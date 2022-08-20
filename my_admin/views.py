from django.http import HttpResponseRedirect
from django.shortcuts import render
from pages_app.models import Gallery, Photo, SEO, NewsAndDiscount, Pages
from cinema_app.models import Movie, Cinema
from .forms import PhotosForm, SEOForm, MovieForm, CinemaForm, NewsAndDiscountForm, PagesForm
from django.core.paginator import Paginator
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.forms import modelformset_factory


class SEOException(Exception):
    def __init__(self, request, way, value_dict):
        self.request = request
        self.way = way
        self.value_dict = value_dict


def change_movie(request, url):
    the_movie = get_object_or_404(Movie, seo__url = url)
    gall = the_movie.photo_list
    quer = Photo.objects.all().filter(gallery=gall)
    if request.method == 'POST':
        photos = PhotosForm(request.POST, request.FILES, queryset=quer)
        movie = MovieForm(request.POST, request.FILES, instance=the_movie)
        seo = SEOForm(request.POST, instance=the_movie.seo)
        for photo in photos:
            if photo.is_valid():
                photo_final = photo.save(commit=False)
                photo_final.gallery = gall
                if photo_final.photo:
                    photo_final.save()
        photos.save()
        url = the_movie.seo.url
        the_movie.seo.url = None
        the_movie.seo.save()
        if not seo.is_valid():
            the_movie.seo.url = url
            the_movie.seo.save()
            return render(request, 'my_admin/add_movie.html', {"photos": photos, "seo": seo, "movie": movie, "the_movie": the_movie})
        new_seo = seo.save()
        the_movie.seo.url = new_seo.url
        the_movie.seo.save()
        seo.save()
        movie.save()
        return HttpResponseRedirect(reverse("movies"))
    else:
        movie = MovieForm(instance=the_movie)
        seo = SEOForm(instance=the_movie.seo)
        photos = PhotosForm(queryset=quer)
        return render(request, "my_admin/add_movie.html", {"photos": photos, "seo": seo, "movie": movie, "the_movie": the_movie})


def get_right_page(request, model, page_type, model_in_page=4):
    try:
        sort_type = int(request.GET.get('type'))
    except TypeError:
        sort_type = -1
    if sort_type == -1:
        model_sum = model.objects.all().order_by("-id")
    elif sort_type == 1:
        model_sum = model.objects.all().order_by("id")
    elif sort_type == 2:
        model_sum = model.objects.all().order_by("name")
    elif sort_type == -2:
        model_sum = model.objects.all().order_by("-name")
    paginator = Paginator(model_sum, model_in_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'my_admin/models.html', {"page": page, "sort_type": sort_type, "type": page_type})


def news(request):
    pass


def cinemas(request):
    return get_right_page(request, Cinema, "cinemas")


def pages(request):
    return get_right_page(request, Pages, "pages")


def movies(request):
    return get_right_page(request, Movie, "movies")


def main_add(request, main_form, name_main_form, plural_name_main_form):
    if request.method == 'POST':
        photos = PhotosForm(request.POST, request.FILES)
        seo = SEOForm(request.POST)
        gallery = Gallery()
        if not seo.is_valid():
            raise SEOException(request, 'my_admin/add_' + name_main_form + '.html',
                               {name_main_form: main_form, 'photos': photos, 'seo': seo})
        if main_form.is_valid():
            gallery.save()
            for photo in photos:
                photo_final = photo.save(commit=False)
                photo_final.gallery = gallery
                if photo_final.photo:
                    photo_final.save()
            final_form = main_form.save(commit=False)
            final_form.photo_list = gallery
            saved_seo = seo.save()
            final_form.seo = saved_seo
            final_form.save()
            return final_form
        else:
            raise ValueError
    else:
        photos = PhotosForm(queryset=Photo.objects.none())
        seo = SEOForm()
        return render(request, 'my_admin/add_' + name_main_form + '.html',
                      {name_main_form: main_form, 'photos': photos, 'seo': seo})


def add_news(request):
    if request.method == 'POST':
        a_news = NewsAndDiscountForm(request.POST, request.FILES)
        try:
            final_news = main_add(request, a_news, "news", "news")
        except SEOException as e:
            return render(e.request, e.way, e.value_dict)
        final_news.type = "News"
        final_news.save()
        return HttpResponseRedirect(reverse('news'))
    else:
        news = NewsAndDiscountForm()
        return main_add(request, news, "news", "news")


def add_movie(request):
    if request.method == 'POST':
        movie = MovieForm(request.POST, request.FILES)
        try:
            final_movie = main_add(request, movie, "movie", "movies")
        except SEOException as e:
            return render(e.request, e.way, e.value_dict)
        final_movie.save()
        return HttpResponseRedirect(reverse('movies'))
    else:
        movie = MovieForm()
        return main_add(request, movie, "movie", "movies")


def add_cinema(request):
    if request.method == 'POST':
        cinema = CinemaForm(request.POST, request.FILES)
        try:
            final_cinema = main_add(request, cinema, "cinema", "cinema")
        except SEOException as e:
            return render(e.request, e.way, e.value_dict)
        final_cinema.save()
        return HttpResponseRedirect(reverse('cinemas'))
    else:
        cinema = CinemaForm()
        return main_add(request, cinema, "cinema", "cinemas")


def add_page(request):
    if request.method == 'POST':
        page = PagesForm(request.POST, request.FILES)
        try:
            final_page = main_add(request, page, "page", "pages")
        except SEOException as e:
            return render(e.request, e.way, e.value_dict)
        final_page.save()
        return HttpResponseRedirect(reverse('pages'))
    else:
        page = CinemaForm()
        return main_add(request, page, "page", "pages")
