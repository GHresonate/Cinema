from django.core.management.base import BaseCommand, CommandError
from user_app.models import CustomUser


class Command(BaseCommand):
    help = 'Creating a supruser first_admin if doesn`t exist, with delivered'

    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help='Email for superuser')
        parser.add_argument('password', type=str, help='Password for superuser')

    def handle(self, *args, **options):
        if not CustomUser.objects.filter(username='first_admin').exists():
            CustomUser.objects.create(name='first_admin', surname='first_admin', username='first_admin',
                                      email=options['email'], password=options['password'], address='add_argument',
                                      card_number='add_argument', language='EN', is_active=True,
                                      is_staff=True, is_superuser='True')

            self.stdout.write(self.style.SUCCESS('User created successful'))
        else:
            self.stdout.write(self.style.NOTICE('User already exist'))
