# Generated by Django 3.2 on 2021-04-18 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_movie_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_id',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
