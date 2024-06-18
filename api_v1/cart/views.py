from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from .cart_service import (
    get_cart_to_user_from_telegram,
    create_get_cart_to_user_from_telegram,
    create_get_cart_item_user_from_telegram,
)
from .serializer import CartSerializer, CartItemSerializer
from ..models import Cart, CartItem


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "cart.html"

    @action(
        detail=False,
        methods=["get"],
        url_path="telegram_id=(?P<telegram_id>[^/.]+)",
        renderer_classes=[TemplateHTMLRenderer],
    )
    def get_cart_by_telegram_id(self, request, telegram_id=None):
        """Получение корзины пользователя телеграмма"""
        serializer = self.get_serializer(get_cart_to_user_from_telegram(telegram_id))
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        cart = create_get_cart_to_user_from_telegram(request)
        serializer = self.get_serializer(cart)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def create(self, request, *args, **kwargs):
        cart_item = create_get_cart_item_user_from_telegram(request)
        serializer = self.get_serializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
