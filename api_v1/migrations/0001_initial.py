# Generated by Django 5.0.6 on 2024-06-10 12:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("description", models.CharField(max_length=255)),
                ("price", models.PositiveIntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("archived", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Товар",
            },
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=30, verbose_name="Имя")),
                ("last_name", models.CharField(max_length=30, verbose_name="Фамилия")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                (
                    "phone",
                    models.PositiveBigIntegerField(
                        blank=True,
                        max_length=11,
                        unique=True,
                        verbose_name="Номер телефона",
                    ),
                ),
                (
                    "geo",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Адрес"
                    ),
                ),
                (
                    "push_email",
                    models.BooleanField(default=False, verbose_name="Рассылка"),
                ),
                (
                    "telegram_id",
                    models.PositiveBigIntegerField(
                        max_length=8, unique=True, verbose_name="ID Пользователя"
                    ),
                ),
            ],
            options={
                "verbose_name": "Пользователь",
            },
        ),
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField(default=1)),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_v1.product",
                        verbose_name="Товар",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_v1.profile",
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Корзина",
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("paid", models.BooleanField(default=False, verbose_name="Оплачено?")),
                (
                    "cart",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_v1.cart",
                        verbose_name="Корзина",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_v1.profile",
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Заказ",
            },
        ),
    ]