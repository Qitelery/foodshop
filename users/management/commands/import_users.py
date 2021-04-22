import requests
from django.core.management import BaseCommand

from users.models import User

URL = 'https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/recipients.json'


class Command(BaseCommand):

    def handle(self, *args, **options):
        response = requests.get(url=URL).json()

        for user in response:
            User.objects.update_or_create(
                id=user['id'],
                defaults={
                    'username': user['email'].split('@')[0],
                    'email': user['email'],
                    'first_name': user['info']['name'],
                    'middle_name': user['info']['patronymic'],
                    'last_name': user['info']['surname'],
                    'phone': user['contacts']['phoneNumber'],
                    'adress': user['city_kladr'],
                    'pass_user': user['password'],
                    'type_account': user['premium'],
                }
            )
        return