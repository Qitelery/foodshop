from rest_framework import serializers
from rest_framework.response import Response

from carts.models import Cart, CartItem
from items.models import Item


class CartSerializer(serializers.ModelSerializer):
    #total_cost = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'items']


class CartItemSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id', 'item', 'quantity', 'price', 'total_price']
        read_only_fields = ['price']

    def create(self, validated_data):
        request = self.context.get("request")
        cart, _ = Cart.objects.get_or_create(user=request.user)
        new_item = CartItem()
        new_item.item_id = self.validated_data['item'].id
        new_item.cart_id = cart.id
        new_item.quantity = self.validated_data['quantity']
        new_item.price = self.validated_data['item'].price

        new_item.save()

        return new_item

    def get_total_price(self, obj):
        return obj.quantity * obj.price
