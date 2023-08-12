# Generated by Django 4.0.5 on 2023-05-28 12:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artax', '0005_alter_book_date_of_registration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_of_registration',
            field=models.DateField(default=datetime.datetime(2023, 5, 28, 15, 55, 59, 887259)),
        ),
        migrations.AlterField(
            model_name='client',
            name='date_of_registration',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='file',
            name='date_of_registration',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_registration',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
