from rest_framework import serializers

from carts.models import Cart, CartItem


class CartSerializer(serializers.ModelSerializer):
    #total_cost = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'items']


class CartItemSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id', 'item', 'quantity', 'total_price']

    def get_total_price(self, obj):
        print(obj)
        return obj['item']['quantity'] * obj['item']['price']
