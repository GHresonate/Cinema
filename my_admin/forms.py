import re
from django import forms
from pages_app.models import SEO, Photo, NewsAndDiscount, Pages
from cinema_app.models import Movie, Cinema
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

    def clean(self):
        cleaned_data = super().clean()
        if not len(re.findall(r'^[^\W]*$', cleaned_data.get('url'))):
            self.add_error("url", "Ссылка должна состоять из одного слова")
        if SEO.objects.filter(url=cleaned_data.get('url')).exists():
            self.add_error("url", "Эта ссылка уже зарегестрирована")
        return cleaned_data


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


class CinemaForm(forms.ModelForm):
    name = forms.CharField(max_length=256)
    description = forms.CharField(widget=forms.Textarea)
    main_photo = forms.ImageField()
    banner_photo = forms.ImageField()

    class Meta:
        model = Cinema
        fields = ('name', 'description', 'main_photo', 'banner_photo')


class NewsAndDiscountForm(forms.ModelForm):
    types = [
        ('News', 'News'),
        ('Discount', 'Discount')
    ]
    type = forms.ChoiceField(choices=types)
    date_published = forms.DateField(input_formats=['%d/%m/%Y'])
    description = forms.CharField(widget=forms.Textarea)
    name = forms.CharField(max_length=256)
    main_photo = forms.ImageField()
    url = forms.URLField()

    class Meta:
        model = NewsAndDiscount
        fields = ('date_published', 'description', 'name', 'main_photo', 'url')


class PagesForm(forms.ModelForm):
    name = forms.CharField(max_length=256)
    description = forms.CharField(widget=forms.Textarea)
    main_photo = forms.ImageField()

    class Meta:
        model = Pages
        fields = ('name', 'description', 'main_photo')