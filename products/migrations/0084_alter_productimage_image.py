# Generated by Django 4.1.13 on 2024-01-24 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0083_alter_order_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]