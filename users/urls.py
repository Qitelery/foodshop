from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from users.views import UserCurrentViewSet, UserRegisterViewSet

urlpatterns = [
    path('current/', UserCurrentViewSet.as_view()),
    path('auth/login/', obtain_auth_token),
    path('auth/register/', UserRegisterViewSet.as_view({'post': 'create'}))
]