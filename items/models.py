from django.db import models

from foodshop.settings import MEDIA_ITEMS_IMAGE_DIR


class Item(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=1024)
    image = models.ImageField(upload_to=MEDIA_ITEMS_IMAGE_DIR)
    weight = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    category = models.PositiveSmallIntegerField(default=None)
