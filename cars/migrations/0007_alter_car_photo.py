# Generated by Django 4.2.1 on 2023-06-01 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_alter_car_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='photo',
            field=models.ImageField(upload_to='cars/'),
        ),
    ]
