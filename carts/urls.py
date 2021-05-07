from django.urls import path

from carts.views import CartViewSet

urlpatterns = [
    path('carts/', CartViewSet.as_view({'get': 'list'})),
]