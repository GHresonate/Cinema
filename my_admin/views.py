from django.http import HttpResponseRedirect
from django.shortcuts import render
from pages_app.models import Gallery, Photo
from .forms import PhotosForm, SEOForm, MovieForm


def main(request):
    return render(request, 'my_admin/main.html')


def set_movie(request):
    if request.method == 'POST':
        photos = PhotosForm(request.POST, request.FILES)
        movie = MovieForm(request.POST, request.FILES)
        seo = SEOForm(request.POST)
        gallery = Gallery()

        if not seo.is_valid():
            raise ValueError

        if movie.is_valid():
            gallery.save()
            for photo in photos:
                photo_final = photo.save(commit=False)
                photo_final.gallery = gallery
                if photo_final.photo:
                    photo_final.save()
            saved_seo = seo.save()
            final_movie = movie.save(commit=False)
            final_movie.seo = saved_seo
            final_movie.photo_list = gallery
            final_movie.save()
            return HttpResponseRedirect('/my_admin')
        else:
            raise ValueError
    else:
        photos = PhotosForm(queryset=Photo.objects.none())
        seo = SEOForm()
        movie = MovieForm()
    return render(request, 'my_admin/movie.html', {'movie': movie, 'photos': photos, 'seo': seo})
