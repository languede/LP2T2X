# Generated by Django 3.2.5 on 2021-10-14 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_rename_ecological_product_is_eco'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=120)),
                ('order_items', models.JSONField()),
                ('total_point', models.IntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=4294967295)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=4294967295),
        ),
    ]