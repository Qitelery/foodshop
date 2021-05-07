from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from users.serializers import UserSerializer, UserRegisterSerializer


class UserRegisterViewSet(ModelViewSet):
    serializer_class = UserRegisterSerializer


class UserCurrentViewSet(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
