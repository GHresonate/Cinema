from django import forms
from pages_app.models import SEO, Photo, Gallery
from cinema_app.models import Movie
from django.forms import modelformset_factory


class PhotoForm(forms.ModelForm):
    photo = forms.ImageField()

    class Meta:
        model = Photo
        fields = ['photo']


PhotosForm = modelformset_factory(Photo, form=PhotoForm, extra=5)


class SEOForm(forms.ModelForm):
    title = forms.CharField(max_length=128)
    url = forms.CharField(max_length=128)
    keywords = forms.CharField(max_length=128)
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = SEO
        fields = ('title', 'url', 'keywords', 'description')


class MovieForm(forms.ModelForm):
    name = forms.CharField(max_length=256)
    description = forms.CharField(widget=forms.Textarea)
    main_photo = forms.ImageField()
    trailer_url = forms.URLField()
    is_2D = forms.BooleanField(required=False)
    is_3D = forms.BooleanField(required=False)
    is_IMAX = forms.BooleanField(required=False)

    class Meta:
        model = Movie
        fields = ('name', 'description', 'main_photo', 'trailer_url', 'is_2D', 'is_3D', 'is_IMAX')
