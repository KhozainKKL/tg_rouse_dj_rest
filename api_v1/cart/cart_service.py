from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api_v1.models import Profile, Cart, Product, CartItem


def get_cart_to_user_from_telegram(telegram_id):
    user = get_object_or_404(Profile, telegram_id=telegram_id)
    cart = Cart.objects.filter(user=user).first()
    if not cart:
        return Response({"detail": "Cart not found."}, status=status.HTTP_404_NOT_FOUND)
    return cart


def create_get_cart_to_user_from_telegram(request):
    user_id = request.data.get("user")
    if not user_id:
        return Response(
            {"detail": "User ID is required."}, status=status.HTTP_400_BAD_REQUEST
        )

    user = get_object_or_404(Profile, telegram_id=user_id)
    cart, created = Cart.objects.get_or_create(user=user)

    for item in request.data.get("items", []):
        product_id = item.get("product")
        quantity = item.get("quantity", 1)
        product = get_object_or_404(Product, pk=product_id)

        cart_item, item_created = CartItem.objects.get_or_create(
            cart=cart, product=product
        )
        if not item_created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()

    return cart


def create_get_cart_item_user_from_telegram(request):
    cart_id = request.data.get('cart')
    if not cart_id:
        return Response({"detail": "User ID is required."}, status=status.HTTP_400_BAD_REQUEST)
    user = get_object_or_404(Profile, telegram_id=cart_id)
    cart, created = Cart.objects.get_or_create(user=user)

    product_id = request.data.get('product')
    quantity = request.data.get('quantity', 1)
    product = get_object_or_404(Product, pk=product_id)

    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity = quantity
    cart_item.save()

    return cart_item
