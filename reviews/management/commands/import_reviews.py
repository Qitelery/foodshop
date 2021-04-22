import requests
from datetime import datetime
from django.core.management import BaseCommand

from reviews.models import Review, User

URL = 'https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/reviews.json'


class Command(BaseCommand):

    def handle(self, *args, **options):
        response = requests.get(url=URL).json()

        for review in response:
            author = User.objects.get(id=review['author'])
            Review.objects.update_or_create(
                id=review['id'],
                defaults={
                    'author': author,
                    'text': review['content'],
                    'created_at': datetime.strptime(review['created_at'], "%Y-%m-%d").date(),
                    'published_at': datetime.strptime(review['published_at'], "%Y-%m-%d").date(),
                    'status': review['status'],
                }
            )
        return