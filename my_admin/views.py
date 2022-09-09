from django.http import HttpResponseRedirect
from django.shortcuts import render
from pages_app.models import Gallery, Photo, SEO, NewsAndDiscount, Pages, BannersInTheTop, Background, MainPage
from cinema_app.models import Movie, Cinema, Hall
from user_app.models import CustomUser
from .forms import PhotosForm, HallForm, SEOForm, MovieForm, CinemaForm, NewsAndDiscountForm, PagesForm, \
    NewsAndDiscBannerForms, TopBannerForms, BackgroundForm, NewsAndDiscInBanner, MainPageForm, ContactForms, \
    UserChangeForm
from django.core.paginator import Paginator
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import permission_required
from django.core.mail import send_mail
from Cinema import create_sessions as cr


class SEOException(Exception):
    def __init__(self, request, way, value_dict):
        self.request = request
        self.way = way
        self.value_dict = value_dict


@permission_required('hav_access_to_admin')
def changeNewsAndDiskInBanner(request):
    if request.method == 'POST':
        top_banners = NewsAndDiscBannerForms(request.POST, request.FILES)
        for banner in top_banners:
            if banner.is_valid():
                banner = banner.save(commit=False)
                if banner.main_photo:
                    banner.save()
        top_banners.save()
        return HttpResponseRedirect(reverse('news'))
    else:
        top_banners = NewsAndDiscBannerForms()
        return render(request, 'my_admin/add_newsintop.html',
                      {'top_banners': top_banners})


@permission_required('hav_access_to_admin')
def change_contacts(request):
    if request.method == 'POST':
        contacts = ContactForms(request.POST, request.FILES)
        for contact in contacts:
            if contact.is_valid():
                contact = contact.save(commit=False)
                if contact.main_photo:
                    contact.save()
        contacts.save()
        return HttpResponseRedirect(reverse('news'))
    else:
        contacts = ContactForms()
        return render(request, 'my_admin/add_contacts.html',
                      {'contacts': contacts})


def change(request, url, model, model_form, model_name, plural_name):
    the_object = get_object_or_404(model, seo__url=url)
    gall = the_object.photo_list
    quer = Photo.objects.all().filter(gallery=gall)
    if request.method == 'POST':
        photos = PhotosForm(request.POST, request.FILES, queryset=quer)
        object = model_form(request.POST, request.FILES, instance=the_object)
        if object.is_valid():
            seo = SEOForm(request.POST, instance=the_object.seo)
            for photo in photos:
                if photo.is_valid():
                    photo_final = photo.save(commit=False)
                    photo_final.gallery = gall
                    if photo_final.photo:
                        photo_final.save()
            photos.save()
            url = the_object.seo.url
            the_object.seo.url = None
            the_object.seo.save()
            if not seo.is_valid():
                the_object.seo.url = url
                the_object.seo.save()
                return render(request, 'my_admin/add_' + model_name + '.html',
                              {"photos": photos, "seo": seo, model_name: object, "the_" + model_name: the_object})
            new_seo = seo.save()
            the_object.seo.url = new_seo.url
            the_object.seo.save()
            seo.save()
            object.save()
            return HttpResponseRedirect(reverse(plural_name))
        else:
            raise ValueError
    else:
        object = model_form(instance=the_object)
        seo = SEOForm(instance=the_object.seo)
        photos = PhotosForm(queryset=quer)
        return render(request, "my_admin/add_" + model_name + ".html",
                      {"photos": photos, "seo": seo, model_name: object, "the_" + model_name: the_object})


@permission_required('hav_access_to_admin')
def change_user(request, username):
    old_user = CustomUser.objects.get(username=username)
    if request.method == 'POST':
        user = UserChangeForm(request.POST, request.FILES, instance=old_user)
        if user.is_valid():
            user.save()
            return HttpResponseRedirect(reverse("users"))
        else:
            print(user.errors)
            raise ValueError
    else:
        user = UserChangeForm(instance=old_user)
        return render(request, 'my_admin/change_user.html', {"another_user": user})


@permission_required('hav_access_to_admin')
def change_main(request):
    the_object = MainPage.objects.get(pk=1)
    if request.method == 'POST':
        object = MainPageForm(request.POST, request.FILES, instance=the_object)
        if object.is_valid():
            seo = SEOForm(request.POST, instance=the_object.seo)
            url = the_object.seo.url
            the_object.seo.url = None
            the_object.seo.save()
            if not seo.is_valid():
                the_object.seo.url = url
                the_object.seo.save()
                return render(request, 'my_admin/change_main.html', {"seo": seo, "main": object})
            new_seo = seo.save()
            the_object.seo.url = new_seo.url
            the_object.seo.save()
            seo.save()
            object.save()
            return HttpResponseRedirect(reverse("news"))
        else:
            print(object.errors)
            raise ValueError
    else:
        object = MainPageForm(instance=the_object)
        seo = SEOForm(instance=the_object.seo)
        return render(request, 'my_admin/change_main.html', {"seo": seo, "main": object})


@permission_required('hav_access_to_admin')
def change_banners(request):
    the_background = Background.objects.get(pk=1)
    if request.method == 'POST':
        background = BackgroundForm(request.POST, request.FILES, instance=the_background)
        top_banners = TopBannerForms(request.POST, request.FILES)
        if background.is_valid():
            for banner in top_banners:

                if banner.is_valid():
                    banner = banner.save(commit=False)
                    if banner.main_photo:
                        banner.save()
            top_banners.save()
            background.save()
            return HttpResponseRedirect(reverse('news'))
        else:
            raise ValueError
    else:
        background = BackgroundForm(instance=the_background)
        top_banners = TopBannerForms()
        return render(request, 'my_admin/add_banners.html',
                      {"background": background, 'top_banners': top_banners, 'the_background': the_background})


@permission_required('hav_access_to_admin')
def change_movie(request, url):
    return change(request, url, Movie, MovieForm, "movie", "movies")

@permission_required('hav_access_to_admin')
def change_hall(request, url):
    return change(request, url, Hall, HallForm, "hall", "cinemas")


@permission_required('hav_access_to_admin')
def change_cinema(request, url):
    the_cinema = get_object_or_404(Cinema, seo__url=url)
    gall = the_cinema.photo_list
    quer = Photo.objects.all().filter(gallery=gall)
    if request.method == 'POST':
        photos = PhotosForm(request.POST, request.FILES, queryset=quer)
        cinema = CinemaForm(request.POST, request.FILES, instance=the_cinema)
        if cinema.is_valid():
            seo = SEOForm(request.POST, instance=the_cinema.seo)
            for photo in photos:
                if photo.is_valid():
                    photo_final = photo.save(commit=False)
                    photo_final.gallery = gall
                    if photo_final.photo:
                        photo_final.save()
            photos.save()
            url = the_cinema.seo.url
            the_cinema.seo.url = None
            the_cinema.seo.save()
            if not seo.is_valid():
                the_cinema.seo.url = url
                the_cinema.seo.save()
                return render(request, 'my_admin/add_cinema.html',
                              {"photos": photos, "seo": seo, "cinema": cinema, "the_cinema": the_cinema})
            new_seo = seo.save()
            the_cinema.seo.url = new_seo.url
            the_cinema.seo.save()
            seo.save()
            cinema.save()
            return HttpResponseRedirect(reverse("cinemas"))
        else:
            raise ValueError
    else:
        cinema = CinemaForm(instance=the_cinema)
        seo = SEOForm(instance=the_cinema.seo)
        photos = PhotosForm(queryset=quer)
        halls = Hall.objects.all().filter(cinema=the_cinema)
        return render(request, "my_admin/add_cinema.html",
                      {"photos": photos, "seo": seo, "cinema": cinema, "the_cinema": the_cinema, "halls":halls})


@permission_required('hav_access_to_admin')
@permission_required('can_change_big_pages')
def change_page(request, url):
    return change(request, url, Pages, PagesForm, "page", "pages")


@permission_required('hav_access_to_admin')
def change_news(request, url):
    return change(request, url, NewsAndDiscount, NewsAndDiscountForm, "news", "news")


@permission_required('hav_access_to_admin')
def change_discount(request, url):
    return change(request, url, NewsAndDiscount, NewsAndDiscountForm, "discount", "discounts")


def get_right_page(request, model, page_type, model_in_page=15):
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


@permission_required('hav_access_to_admin')
def users(request):
    try:
        sort_type = int(request.GET.get('type'))
    except TypeError:
        sort_type = -1
    if request.user.is_superuser:
        if sort_type == -1:
            model_sum = CustomUser.objects.all().order_by("-id")
        elif sort_type == 1:
            model_sum = CustomUser.objects.all().order_by("id")
        elif sort_type == 2:
            model_sum = CustomUser.objects.all().order_by("email")
        elif sort_type == -2:
            model_sum = CustomUser.objects.all().order_by("-email")
    else:
        if sort_type == -1:
            model_sum = CustomUser.objects.all().filter(is_staff=False).filter(is_superuser=False).order_by("-id")
        elif sort_type == 1:
            model_sum = CustomUser.objects.all().filter(is_staff=False).filter(is_superuser=False).order_by("id")
        elif sort_type == 2:
            model_sum = CustomUser.objects.all().filter(is_staff=False).filter(is_superuser=False).order_by("email")
        elif sort_type == -2:
            model_sum = CustomUser.objects.all().filter(is_staff=False).filter(is_superuser=False).order_by("-email")
    paginator = Paginator(model_sum, 15)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'my_admin/users.html', {"page": page, "sort_type": sort_type})


@permission_required('hav_access_to_admin')
def news(request):
    try:
        sort_type = int(request.GET.get('type'))
    except TypeError:
        sort_type = -1
    if sort_type == -1:
        model_sum = NewsAndDiscount.objects.all().filter(type="News").order_by("-id")
    elif sort_type == 1:
        model_sum = NewsAndDiscount.objects.all().filter(type="News").order_by("id")
    elif sort_type == 2:
        model_sum = NewsAndDiscount.objects.all().filter(type="News").order_by("name")
    elif sort_type == -2:
        model_sum = NewsAndDiscount.objects.all().filter(type="News").order_by("-name")
    paginator = Paginator(model_sum, 15)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'my_admin/models.html', {"page": page, "sort_type": sort_type, "type": "news"})


@permission_required('hav_access_to_admin')
def discounts(request):
    try:
        sort_type = int(request.GET.get('type'))
    except TypeError:
        sort_type = -1
    if sort_type == -1:
        model_sum = NewsAndDiscount.objects.all().filter(type="Discount").order_by("-id")
    elif sort_type == 1:
        model_sum = NewsAndDiscount.objects.all().filter(type="Discount").order_by("id")
    elif sort_type == 2:
        model_sum = NewsAndDiscount.objects.all().filter(type="Discount").order_by("name")
    elif sort_type == -2:
        model_sum = NewsAndDiscount.objects.all().filter(type="Discount").order_by("-name")
    paginator = Paginator(model_sum, 15)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'my_admin/models.html', {"page": page, "sort_type": sort_type, "type": "discounts"})


@permission_required('hav_access_to_admin')
def cinemas(request):
    return get_right_page(request, Cinema, "cinemas")


@permission_required('hav_access_to_admin')
def pages(request):
    return get_right_page(request, Pages, "pages")


@permission_required('hav_access_to_admin')
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
            return final_form
        else:
            print(main_form.errors)
            raise ValueError
    else:
        photos = PhotosForm(queryset=Photo.objects.none())
        seo = SEOForm()
        return render(request, 'my_admin/add_' + name_main_form + '.html',
                      {name_main_form: main_form, 'photos': photos, 'seo': seo})


@permission_required('hav_access_to_admin')
def add_hall(request, cinema_number):
    if request.method == 'POST':
        cinema = get_object_or_404(Cinema, id=cinema_number)
        hall = HallForm(request.POST, request.FILES)
        try:
            final_hall = main_add(request, hall, "hall", "halls")
        except SEOException as e:
            return render(e.request, e.way, e.value_dict)
        final_hall.cinema = cinema
        final_hall.save()
        return HttpResponseRedirect(reverse('news'))
    else:
        hall = HallForm()
        return main_add(request, hall, "hall", "halls")


@permission_required('hav_access_to_admin')
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


@permission_required('hav_access_to_admin')
def add_disc(request):
    if request.method == 'POST':
        a_disc = NewsAndDiscountForm(request.POST, request.FILES)
        try:
            final_disc = main_add(request, a_disc, "discount", "discounts")
        except SEOException as e:
            return render(e.request, e.way, e.value_dict)
        final_disc.type = "Discount"
        final_disc.save()
        return HttpResponseRedirect(reverse('discounts'))
    else:
        disc = NewsAndDiscountForm()
        return main_add(request, disc, "discount", "discounts")


@permission_required('hav_access_to_admin')
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


@permission_required('hav_access_to_admin')
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


@permission_required('hav_access_to_admin')
@permission_required('can_change_big_pages')
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


def create_sessions(request):
    cr.main()


def send_email(request):
    send_mail('test','<h1>testtt</h1>',from_email=None, recipient_list=["test.for.site.dja@gmail.com",])
