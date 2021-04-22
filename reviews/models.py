from django.db import models
from users.models import User


class Review(models.Model):
    author = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    text = models.TextField(max_length=1024)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    published_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    status = models.CharField(max_length=64)