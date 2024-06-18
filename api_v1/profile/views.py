from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from .serializer import ProfileSerializer
from ..models import Profile


class ProfileViewSet(viewsets.ModelViewSet):
    """Получение всех пользователей магазина"""

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    renderer_classes = [TemplateHTMLRenderer]
    template_name = "index.html"

    @action(methods=["get"], detail=True, renderer_classes=[TemplateHTMLRenderer])
    def telegram(self, request, pk=None):
        """Получение конкретного пользователя по его id в телеграмм"""
        user = Profile.objects.get(telegram_id=pk)
        return Response(ProfileSerializer(user).data)
