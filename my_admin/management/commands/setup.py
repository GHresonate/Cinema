from django.core.management.base import BaseCommand, CommandError
from user_app.models import CustomUser
from pages_app.models import Background, MainPage, SEO, Pages, Gallery
import environ

env = environ.Env(
    DEBUG=(bool, False)
)


class Command(BaseCommand):
    help = 'Creating a supruser if doesn`t exist'

    def handle(self, *args, **options):
        if not CustomUser.objects.filter(is_superuser=True).exists():
            CustomUser.objects.create_superuser(name='first_admin', surname='first_admin', username=env('username'),
                                      email=env('user_email'), password=env('user_password'), address='add_argument',
                                      card_number='add_argument', language='EN', is_active=True,)

            self.stdout.write(self.style.SUCCESS('User created successfully'))
        else:
            self.stdout.write(self.style.NOTICE('User already exist'))
        if not Background.objects.all().exists():
            Background.objects.create(is_photo=False, color='#00FFFF')
            self.stdout.write(self.style.SUCCESS('Background created successfully'))
        else:
            self.stdout.write(self.style.NOTICE('Background already exist'))
        if not MainPage.objects.all().exists():
            seo=SEO.objects.create(title='Main page', url='main_page',definition='sdfgsfgs',keywords='main')
            MainPage.objects.create(seo_text='rgfkbspb',seo=seo,phone_number='+380966666666', phone_number2='+380977777777')
            self.stdout.write(self.style.SUCCESS('MainPage created successfully'))
        else:
            self.stdout.write(self.style.NOTICE('MainPage already exist'))

        if not Pages.objects.filter(name_ru='Главная страница').exists():
            seo = SEO.objects.create(title='Main page', url='main_page_of_the_cinema', definition='sdfgsfgs',keywords='main')
            gallery = Gallery.objects.create()
            Pages.objects.create(name_ru="Главная страница", name_uk='Головна сторінка', description_ru="-",description_uk='-', main_photo='-',is_active=True, seo=seo,photo_list=gallery)
            self.stdout.write(self.style.SUCCESS('Main page created successfully'))
        else:
            self.stdout.write(self.style.NOTICE('Main page already exist'))
