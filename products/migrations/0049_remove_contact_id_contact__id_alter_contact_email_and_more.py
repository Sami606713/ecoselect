# Generated by Django 4.1.13 on 2023-12-19 10:14

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0048_alter_contact_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='id',
        ),
        migrations.AddField(
            model_name='contact',
            name='_id',
            field=djongo.models.fields.ObjectIdField(auto_created=True, default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='msg',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='+92*********', max_length=15),
        ),
    ]