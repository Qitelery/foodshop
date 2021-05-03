from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from users.views import UserCurrentViewSet

urlpatterns = [
    path('current/', UserCurrentViewSet.as_view({'get': 'list', 'put': 'update', 'patch': 'partial_update'})),
    path('auth/login/', obtain_auth_token),
]