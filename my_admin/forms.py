import re
from django import forms
from pages_app.models import SEO, Photo, NewsAndDiscount, Pages, BannersInTheTop, Background, NewsAndDiscInBanner, \
    MainPage, Contact
from user_app.models import CustomUser
from cinema_app.models import Movie, Cinema, Hall
from django.forms import modelformset_factory


class UserChangeForm(forms.ModelForm):
    name = forms.CharField(max_length=256)
    surname = forms.CharField(max_length=256)
    username = forms.CharField(max_length=256)
    email = forms.EmailField()
    address = forms.CharField(max_length=256)
    card_number = forms.IntegerField()
    languishes = [
        ('UA', 'Ukrainian'),
        ('EN', 'English'),
        ('RU', 'Russian')
    ]
    language = forms.ChoiceField(choices=languishes)
    genders = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Different', 'Different'),
        ('Don`t say', 'Don`t say'),
    ]
    gender = forms.ChoiceField(choices=genders)
    is_active = forms.BooleanField(required=False)
    is_superuser = forms.BooleanField(required=False)
    is_staff = forms.BooleanField(required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'name', 'surname', 'address', 'card_number', 'language', 'gender', 'is_active',
                  'is_superuser', 'is_staff')


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
    definition = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = SEO
        fields = ('title', 'url', 'keywords', 'definition')

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
    trailer_url = forms.CharField(max_length=256)
    is_2D = forms.BooleanField(required=False)
    is_3D = forms.BooleanField(required=False)
    is_IMAX = forms.BooleanField(required=False)
    realise_date = forms.DateField(localize=True, widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Movie
        fields = ('name', 'description', 'main_photo', 'trailer_url', 'is_2D', 'is_3D', 'is_IMAX', 'realise_date')


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


class BannersInTheTopForm(forms.ModelForm):
    main_photo = forms.ImageField(required=True)
    text = forms.CharField(widget=forms.Textarea, required=True)
    url = forms.CharField(max_length=256, required=True)

    class Meta:
        model = BannersInTheTop
        fields = ('main_photo', 'text', 'url')


TopBannerForms = modelformset_factory(BannersInTheTop, form=BannersInTheTopForm, extra=5, max_num=5, can_delete=True)


class BackgroundForm(forms.ModelForm):
    main_photo = forms.ImageField(required=False)
    type = forms.BooleanField(required=False)
    color = forms.CharField(max_length=32, required=False, widget=forms.TextInput(attrs={'type': 'color'}))

    class Meta:
        model = Background
        fields = ('main_photo', 'color')


class NewsAndDiscInBannerForm(forms.ModelForm):
    main_photo = forms.ImageField()
    trailer_url = forms.CharField(max_length=64)

    class Meta:
        model = NewsAndDiscInBanner
        fields = ('main_photo', 'trailer_url')


NewsAndDiscBannerForms = modelformset_factory(NewsAndDiscInBanner, form=NewsAndDiscInBannerForm, extra=5, max_num=5,
                                              can_delete=True)


class ContactForm(forms.ModelForm):
    main_photo = forms.ImageField()
    name = forms.CharField(max_length=256)
    address = forms.CharField(widget=forms.Textarea)
    coordinate = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Contact
        fields = ('main_photo', 'name', 'address', 'coordinate')


ContactForms = modelformset_factory(Contact, form=ContactForm, can_delete=True, extra=5, max_num=5)


class MainPageForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=64)
    phone_number2 = forms.CharField(max_length=64)
    seo_text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = MainPage
        fields = ('phone_number', 'phone_number2', 'seo_text')


class HallForm(forms.ModelForm):
    number = forms.IntegerField()
    name = forms.CharField(max_length=128)
    created_date = forms.DateField(input_formats=['%d/%m/%Y'],localize=True, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    description = forms.CharField(widget=forms.Textarea)
    scheme = forms.JSONField()
    main_photo = forms.ImageField()

    class Meta:
        model = Hall
        fields = ('number', 'name', 'created_date', 'description', 'scheme', 'main_photo')
