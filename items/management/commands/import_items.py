import requests
from django.core.management import BaseCommand

from items.models import Item

URL = 'https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/foodboxes.json'


class Command(BaseCommand):
    def handle(self, *args, **options):
        response = requests.get(url=URL).json()

        for item in response:
            Item.objects.update_or_create(
                id=item['id'],
                defaults={
                    'title': item['title'],
                    'description': item['description'],
                    'image': '',
                    'weight': item['weight_grams'],
                    'price': item['price'],
                    'category': item['cat'],
                }
            )
        return