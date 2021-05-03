from django.db import models
from users.models import User


class Review(models.Model):
    author = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    text = models.TextField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField()
    status = models.CharField(max_length=64)