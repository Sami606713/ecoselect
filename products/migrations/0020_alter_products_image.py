# Generated by Django 4.1.13 on 2023-12-08 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(default='', upload_to="{% static 'products/images' %}"),
        ),
    ]
