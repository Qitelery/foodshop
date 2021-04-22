from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from items.models import Item


@api_view(['GET'])
def get_item(request, pk):
    try:
        item = Item.objects.get(id=pk)
        return Response({
            'id': item.id,
            'title': item.title,
            'description': item.description,
            'image': str(item.image),
            'weight_grams': item.weight,
            'price': item.price,
            'category': item.category,
        })
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
