# Generated by Django 4.1.13 on 2024-01-12 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0070_remove_order__id_order_id_order_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='item_json',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='address',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
