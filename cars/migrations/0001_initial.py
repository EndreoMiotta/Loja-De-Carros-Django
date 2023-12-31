# Generated by Django 4.2.1 on 2023-05-28 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model', models.CharField(blank=True, max_length=200, null=True)),
                ('brand', models.CharField(blank=True, max_length=200, null=True)),
                ('factory_year', models.IntegerField()),
                ('model_year', models.IntegerField()),
                ('value', models.FloatField()),
            ],
        ),
    ]
