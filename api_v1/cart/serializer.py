from rest_framework import serializers

from api_v1.models import Product, Profile, Cart, CartItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class CartItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    product_details = ProductSerializer(source="product", read_only=True)

    class Meta:
        model = CartItem
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    user = ProfileSerializer()
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = "__all__"
