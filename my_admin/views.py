from django.http import HttpResponseRedirect
from django.shortcuts import render
from pages_app.models import Gallery, Photo, SEO, NewsAndDiscount, Pages, BannersInTheTop, Background, MainPage
from cinema_app.models import Movie, Cinema, Hall, Session
from user_app.models import CustomUser
from .forms import PhotosForm, HallForm, SEOForm, MovieForm, CinemaForm, NewsAndDiscountForm, PagesForm, \
    NewsAndDiscBannerForms, TopBannerForms, BackgroundForm, NewsAndDiscInBanner, MainPageForm, ContactForms, \
    UserChangeForm, TemplateForm
from django.core.paginator import Paginator
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Template
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import permission_required
from django.core.mail import send_mail
from Cinema import create_sessions as cr
import json
from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.http import JsonResponse
from datetime import date, timedelta


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
        return HttpResponseRedirect(reverse('statistic'))
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
        return HttpResponseRedirect(reverse('statistic'))
    else:
        contacts = ContactForms()
        return render(request, 'my_admin/add_contacts.html',
                      {'contacts': contacts})


@permission_required('hav_access_to_admin')
def delete_by_seo(request, url):
    seo = SEO.objects.get(url=url)



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
        print(request.POST)
        object = MainPageForm(request.POST, instance=the_object)
        if object.is_valid():
            seo = SEOForm(request.POST, instance=the_object.seo)
            url = the_object.seo.url
            the_object.seo.url = None
            the_object.seo.save()
            if not seo.is_valid():
                print(seo.errors)
                the_object.seo.url = url
                the_object.seo.save()
                return render(request, 'my_admin/change_main.html', {"seo": seo, "main": object})
            new_seo = seo.save()
            the_object.seo.url = new_seo.url
            the_object.seo.save()
            seo.save()
            object.save()
            print(object)
            return HttpResponseRedirect(reverse("statistic"))
        else:
            print(object.errors)
            raise ValueError
    else:
        object = MainPageForm(instance=the_object)
        seo = SEOForm(instance=the_object.seo)
        return render(request, 'my_admin/change_main.html', {"seo": seo, "main": object})


@permission_required('hav_access_to_admin')
def change_banners(request):
    the_background = Background.objects.all()[0]
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
            return HttpResponseRedirect(reverse('statistic'))
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
                      {"photos": photos, "seo": seo, "cinema": cinema, "the_cinema": the_cinema, "halls": halls})


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
        return HttpResponseRedirect(reverse('statistic'))
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
        page = PagesForm()
        return main_add(request, page, "page", "pages")


def create_sessions(request):
    cr.main()


@permission_required('hav_access_to_admin')
def choose_users(request):
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
    return render(request, 'my_admin/choose_users.html', {"page": page, "sort_type": sort_type})


@permission_required('hav_access_to_admin')
def send_email(request):
    try:
        information_about_sending = json.load(request)
        template_id = information_about_sending['id']
        template = Template.objects.get(id=template_id)
        if information_about_sending['for_chosen']:
            chosen_emails = information_about_sending['chosen']
            users_for_send = []
            for user_id in chosen_emails:
                if user_id:
                    user = CustomUser.objects.get(id=int(user_id))
                    users_for_send.append(user)
        else:
            users_for_send = CustomUser.objects.all()
        msg = EmailMessage(template.name, open(template.file.path, "r").read(), to=users_for_send)
        msg.content_subtype = "html"
        msg.send()
    except Exception as e:
        return JsonResponse(json.dumps({'value': e}), status=500, safe=False)
    return JsonResponse(json.dumps({'value': 'Все письма отосланы'}), status=200, safe=False)


@permission_required('hav_access_to_admin')
def delete_hall(request, hall_id):
    hall_for_delete = Hall.objects.get(id=hall_id)
    hall_for_delete.delete()
    return render(request, 'my_admin/succsess_delete.html')


@permission_required('hav_access_to_admin')
def delete_cinema(request, cinema_id):
    cinema_for_delete = Cinema.objects.get(id=cinema_id)
    cinema_for_delete.delete()
    return render(request, 'my_admin/succsess_delete.html')


@permission_required('hav_access_to_admin')
def delete_movie(request, movie_id):
    movie_for_delete = Movie.objects.get(id=movie_id)
    movie_for_delete.delete()
    return render(request, 'my_admin/succsess_delete.html')

@permission_required('hav_access_to_admin')
def delete_page(request, page_id):
    pages_for_delete = Pages.objects.get(id=page_id)
    if not pages_for_delete.is_active:
        pages_for_delete.delete()
        return render(request, 'my_admin/succsess_delete.html')
    return render(request, 'my_admin/cant_delete.html')



@permission_required('hav_access_to_admin')
def delete_discounts(request, disc_id):
    disc_for_delete = NewsAndDiscount.objects.get(id=disc_id)
    if not disc_for_delete.is_active:
        disc_for_delete.delete()
        return render(request, 'my_admin/succsess_delete.html')
    return render(request, 'my_admin/cant_delete.html')


@permission_required('hav_access_to_admin')
def delete_news(request, news_id):
    news_for_delete = NewsAndDiscount.objects.get(id=news_id)
    if not news_for_delete.is_active:
        news_for_delete.delete()
        return render(request, 'my_admin/succsess_delete.html')
    return render(request, 'my_admin/cant_delete.html')



@permission_required('hav_access_to_admin')
def prepare_sending(request):
    template = TemplateForm()
    return render(request, 'my_admin/email_sending.html', {'template': template})


@permission_required('hav_access_to_admin')
def delete_user(request, user_id):
    the_user = CustomUser.objects.get(id=user_id)
    username = the_user.username
    if the_user.is_superuser:
        raise ValueError
    the_user.delete()
    return render(request, 'my_admin/succsess_user_delete.html', {'username': username})


@permission_required('hav_access_to_admin')
def statistic(request):
    users = CustomUser.objects.all().count()
    return render(request, 'my_admin/index.html', {'users': users})


@permission_required('hav_access_to_admin')
def get_templates(request):
    templates = Template.objects.all()
    result = {}
    names = []
    id_for_result = []
    url = []
    for template in templates:
        names.append(template.name)
        id_for_result.append(template.id)
        url.append(template.file.url)
    result['names'] = names
    result['id'] = id_for_result
    result['url'] = url
    return JsonResponse(json.dumps(result), status=200, safe=False)


@permission_required('hav_access_to_admin')
def delete_template(request):
    id_for_delete = json.load(request)['id']
    template = Template.objects.get(id=id_for_delete)
    template.delete()
    return get_templates(request)


@permission_required('hav_access_to_admin')
def add_template(request):
    if request.method == 'POST':
        template = TemplateForm(request.POST, request.FILES)
        template.save()
        templates = Template.objects.all()
        if templates.count() >= 6:
            templates[0].delete()
        return get_templates(request)


@permission_required('hav_access_to_admin')
def get_movies(request):
    all_sessions = Session.objects.count()
    movies = Movie.objects.all()
    label = []
    data = []
    colors = ['#f56954', '#00a65a', '#f39c12', '#00c0ef', '#3c8dbc', '#d2d6de']
    backgroundColor = []
    for movie in movies:
        label.append(movie.name)
        percent = Session.objects.all().filter(movie=movie).count()
        data.append(percent)
        backgroundColor.append(colors[movie.id % len(colors)])
    result = {'labels': label, 'datasets': [{'data': data, 'backgroundColor': backgroundColor}]}
    return JsonResponse(json.dumps(result), status=200, safe=False)


@permission_required('hav_access_to_admin')
def get_sessions(request):
    AMOUNT_DAYS = 40
    START_DAY = 20
    data = []
    labels = []
    first_day = date.today()-timedelta(days=START_DAY)
    for first in range(AMOUNT_DAYS):
        day = first_day + timedelta(days=first)
        in_day = Session.objects.all().filter(date=day).count()
        labels.append(str(day.day) + '.' + str(day.month))
        data.append(in_day)
    result = {'data': data, 'labels': labels}
    return JsonResponse(json.dumps(result), status=200, safe=False)


@permission_required('hav_access_to_admin')
def get_users_gender(request):
    users = CustomUser.objects.all()
    male = 0
    female = 0
    different = 0
    label = ['Males', 'Females', 'Different']
    for user in users:
        if user.gender == 'Male':
            male += 1
        elif user.gender == 'Female':
            female += 1
        else:
            different += 1
    colors = ['#f56954', '#00a65a', '#f39c12']
    result = {'labels': label, 'datasets': [{'data': [male, female, different], 'backgroundColor': colors}]}
    return JsonResponse(json.dumps(result), status=200, safe=False)
