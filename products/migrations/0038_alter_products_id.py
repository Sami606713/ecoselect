# Generated by Django 4.1.13 on 2023-12-17 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0037_remove_products_item_id_products_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='id',
            field=models.AutoField(default=2, primary_key=True, serialize=False),
        ),
    ]