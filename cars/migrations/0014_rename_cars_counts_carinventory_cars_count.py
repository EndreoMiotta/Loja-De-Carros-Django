# Generated by Django 4.2.1 on 2023-07-06 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0013_carinventory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carinventory',
            old_name='cars_counts',
            new_name='cars_count',
        ),
    ]
