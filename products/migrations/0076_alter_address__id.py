# Generated by Django 4.1.13 on 2024-01-15 19:27

from django.db import migrations
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0075_order_address_alter_address__id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='_id',
            field=djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
