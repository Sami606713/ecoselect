# Generated by Django 4.1.13 on 2023-12-17 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0032_alter_products_item_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='item_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]