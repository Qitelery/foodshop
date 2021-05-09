from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from carts.models import Cart, CartItem
from carts.serializers import CartSerializer, CartItemSerializer
from items.models import Item


class CartViewSet(ReadOnlyModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]


class CartItemViewSet(ModelViewSet):

    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_item = CartItemSerializer(data=request.data)
        if cart_item.is_valid():
            item = Item.objects.get(id=request.data.get('item'))
            new_cart_item = CartItem.objects.create(
                item_id=cart_item.data['item'],
                cart_id=cart.id,
                quantity=cart_item.data['quantity'],
                price=item.price,
            )
            return Response(CartItemSerializer(new_cart_item).data)
