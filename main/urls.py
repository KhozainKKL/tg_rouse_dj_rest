"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from api_v1.cart.views import CartViewSet, CartItemViewSet
from api_v1.product.views import ProductViewSet
from rest_framework import routers
from api_v1.profile.views import ProfileViewSet

router = routers.SimpleRouter()
router.register(r"product", ProductViewSet)
router.register(r"profile", ProfileViewSet)
router.register(r"carts", CartViewSet)
router.register(r"cart-items", CartItemViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
    path("cart/", TemplateView.as_view(template_name="cart.html"), name="cart"),
    path("search/", TemplateView.as_view(template_name="search.html"), name="search"),
    path("order/", TemplateView.as_view(template_name="order.html"), name="order"),
    path("auth/", TemplateView.as_view(template_name="auth.html"), name="auth"),
    path("profile/", TemplateView.as_view(template_name="profile.html"), name="profile"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
