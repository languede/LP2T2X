# Generated by Django 3.2.5 on 2021-10-16 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_product_price_degree'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ecoinfo',
            field=models.TextField(blank=True, null=True),
        ),
    ]
