from django.db import models


class Product(models.Model):
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    price = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Profile(models.Model):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    first_name = models.CharField(max_length=30, verbose_name="Имя")
    last_name = models.CharField(max_length=30, verbose_name="Фамилия")
    email = models.EmailField(verbose_name="Email")
    phone = models.PositiveBigIntegerField(
        unique=True,
        blank=True,
        null=True,
        max_length=11,
        verbose_name="Номер телефона",
    )
    geo = models.CharField(max_length=255, blank=True, null=True, verbose_name="Адрес")
    push_email = models.BooleanField(default=False, verbose_name="Рассылка")
    telegram_id = models.PositiveBigIntegerField(
        unique=True, max_length=8, verbose_name="ID Пользователя"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Cart(models.Model):
    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    user = models.ForeignKey(
        Profile, on_delete=models.CASCADE, verbose_name="Пользователь", null=True
    )

    def __str__(self):
        return f"Корзина {self.id} пользователя {self.user}"


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, related_name="items", on_delete=models.CASCADE, null=True
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Товар", null=True
    )
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} в корзине {self.cart.id}"


class Order(models.Model):
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Закаы"

    user = models.ForeignKey(
        Profile, on_delete=models.CASCADE, verbose_name="Пользователь", null=True
    )
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, verbose_name="Корзина", null=True
    )
    paid = models.BooleanField(default=False, verbose_name="Оплачено?")

    def __str__(self):
        return self.user
