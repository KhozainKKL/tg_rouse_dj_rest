from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializer import ProfileSerializer
from ..models import Profile


class ProfileViewSet(viewsets.ModelViewSet):
    """Получение всех пользователей магазина"""

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @action(methods=["get"], detail=True)
    def telegram(self, request, pk=None):
        """Получение конкретного пользователя по его id в телеграмм"""
        user = Profile.objects.get(telegram_id=pk)
        return Response(ProfileSerializer(user).data)
