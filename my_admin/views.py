from django.http import HttpResponseRedirect
from django.shortcuts import render
from pages_app.models import Gallery, Photo, SEO, NewsAndDiscount
from cinema_app.models import Movie, Cinema
from .forms import PhotosForm, SEOForm, MovieForm, CinemaForm, NewsAndDiscountForm, PagesForm
from django.core.paginator import Paginator
from django.urls import reverse
from django.shortcuts import get_object_or_404


def get_movie(request, url):
    the_movie = get_object_or_404(Movie, seo__url=url)
    old_photos = Photo.objects.all().filter(gallery=the_movie.photo_list)
    photos = PhotosForm(queryset=Photo.objects.all().filter(gallery=the_movie.photo_list))
    seo = SEOForm(instance=the_movie.seo)
    movie = MovieForm(instance=the_movie)
    if request.method == 'POST':
        new_photos = PhotosForm(request.POST, request.FILES)
        new_movie = MovieForm(request.POST, request.FILES)
        new_seo = SEOForm(request.POST)
        gallery = the_movie.photo_list
        if new_movie.is_valid():
            for photo in old_photos:
                photo.delete()
            for photo in new_photos:
                photo_final = photo.save(commit=False)
                photo_final.gallery = gallery
                if photo_final.photo:
                    photo_final.save()
            url = the_movie.seo.url
            the_movie.seo.url = None
            the_movie.seo.save()
            if not new_seo.is_valid():
                the_movie.seo.url = url
                the_movie.seo.save()
                return render(request, 'my_admin/add_movie.html',
                              {'movie': new_movie, 'photos': new_photos, 'seo': new_seo})
            new_seo = new_seo.save()
            the_movie.seo = new_seo
            the_movie.save()

            new_movie = new_movie.save(commit=False)
            new_data = {}
            for x in movie.changed_data:
                new_data[x] = new_movie.__dict__[x]
            movie_id = the_movie.id
            Movie.objects.filter(id=movie_id).update(**new_data)
            return HttpResponseRedirect(reverse('movies'))
        # return HttpResponseRedirect(reverse('name', args=(year,)))
        else:
            raise ValueError
    return render(request, 'my_admin/add_movie.html', {'movie': movie, 'photos': photos, 'seo': seo})


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


def movies(request):
    return get_right_page(request, Movie, "movies")


def main_add(request, main_form, name_main_form, plural_name_main_form):
    if request.method == 'POST':
        photos = PhotosForm(request.POST, request.FILES)
        seo = SEOForm(request.POST)
        gallery = Gallery()
        if not seo.is_valid():
            return render(request, 'my_admin/add_' + name_main_form + '.html',
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
        final_news = main_add(request, a_news, "news", "news")
        final_news.type = "News"
        final_news.save()
        return HttpResponseRedirect(reverse('news'))
    else:
        news = NewsAndDiscountForm()
        return main_add(request, news, "news", "news")


def add_movie(request):
    if request.method == 'POST':
        movie = MovieForm(request.POST, request.FILES)
        final_movie = main_add(request, movie, "movie", "movies")
        final_movie.save()
        return HttpResponseRedirect(reverse('movies'))
    else:
        movie = MovieForm()
        return main_add(request, movie, "movie", "movies")


def add_cinema(request):
    if request.method == 'POST':
        cinema = CinemaForm(request.POST, request.FILES)
        final_cinema = main_add(request, cinema, "cinema", "cinema")
        final_cinema.save()
        return HttpResponseRedirect(reverse('cinemas'))
    else:
        cinema = CinemaForm()
        return main_add(request, cinema, "cinema", "cinemas")


def add_page(request):
    if request.method == 'POST':
        page = PagesForm(request.POST, request.FILES)
        final_page = main_add(request, page, "page", "pages")
        final_page.save()
        return HttpResponseRedirect(reverse('pages'))
    else:
        page = CinemaForm()
        return main_add(request, page, "page", "pages")
