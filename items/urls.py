from django.urls import path

from items.views import get_item

urlpatterns = [
    path('item/<int:pk>/', get_item),
]