# Generated by Django 4.2.16 on 2024-09-29 21:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payment", "0004_order_orderitem"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="shipped",
            field=models.BooleanField(default=False),
        ),
    ]
