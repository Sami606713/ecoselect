# Generated by Django 4.1.13 on 2024-01-17 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0080_remove_order_id_alter_order_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.CharField(default='', max_length=250, unique=True),
        ),
    ]
