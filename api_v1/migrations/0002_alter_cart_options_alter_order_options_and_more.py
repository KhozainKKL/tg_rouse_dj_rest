# Generated by Django 5.0.6 on 2024-06-11 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api_v1", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cart",
            options={"verbose_name": "Корзина", "verbose_name_plural": "Корзины"},
        ),
        migrations.AlterModelOptions(
            name="order",
            options={"verbose_name": "Заказ", "verbose_name_plural": "Закаы"},
        ),
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name": "Товар", "verbose_name_plural": "Товары"},
        ),
        migrations.AlterModelOptions(
            name="profile",
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
        migrations.AlterField(
            model_name="profile",
            name="phone",
            field=models.PositiveBigIntegerField(
                blank=True,
                max_length=11,
                null=True,
                unique=True,
                verbose_name="Номер телефона",
            ),
        ),
    ]
