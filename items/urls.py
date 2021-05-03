from django.urls import path

from items.views import ItemViewSet

urlpatterns = [
    path('', ItemViewSet.as_view()),
]