# Generated by Django 4.0.3 on 2022-05-12 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_payment_orderproduct_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]