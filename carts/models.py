from django.db import models

from items.models import Item
from users.models import User


class Cart(models.Model):
    user = models.ForeignKey(User, related_name='carts', on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, related_name='carts', through='CartItem')


class CartItem(models.Model):
    item = models.ForeignKey(Item, related_name='cartitems', on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, related_name='cartitems', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)