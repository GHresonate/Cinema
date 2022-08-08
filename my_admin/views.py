from django.http import HttpResponseRedirect
from django.shortcuts import render
from pages_app.models import Gallery, Photo
from .forms import PhotosForm, SEOForm, MovieForm


def set_movie(request):
    if request.method == 'POST':
        photos = PhotosForm(request.POST, request.FILES)
        movie = MovieForm(request.POST, request.FILES)
        seo = SEOForm(request.POST)
        gallery = Gallery()
        gallery.save()
        if seo.is_valid():
            saved_seo = seo.save()
        for photo in photos:
            photo_final = photo.save(commit=False)
            photo_final.gallery = gallery
            if photo_final.photo:
                photo_final.save()
        if movie.is_valid():
            final_movie = movie.save(commit=False)
        else:
            print(movie.errors)
        final_movie.seo = saved_seo
        final_movie.photo_list = gallery
        final_movie.save()
        return HttpResponseRedirect('/my_admin')
    else:
        photos = PhotosForm(queryset=Photo.objects.none())
        seo = SEOForm()
        movie = MovieForm()

    return render(request, 'my_admin/movie.html', {'movie': movie, 'photos': photos, 'seo': seo})
