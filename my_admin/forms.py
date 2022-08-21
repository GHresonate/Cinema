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


PhotosForm = modelformset_factory(Photo, form=PhotoForm, extra=5, max_num=5, can_delete=True)


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
    description = forms.CharField(widget=forms.Textarea)
    name = forms.CharField(max_length=256)
    main_photo = forms.ImageField()
    is_active = forms.BooleanField(required=False)
    trailer_url = forms.URLField()
    date_published = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = NewsAndDiscount
        fields = ('description', 'date_published', 'name', 'main_photo', 'is_active', 'trailer_url')


class PagesForm(forms.ModelForm):
    name = forms.CharField(max_length=256)
    description = forms.CharField(widget=forms.Textarea)
    main_photo = forms.ImageField()

    class Meta:
        model = Pages
        fields = ('name', 'description', 'main_photo')
