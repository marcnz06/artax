# Generated by Django 4.0.5 on 2023-05-29 14:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artax', '0006_alter_book_date_of_registration_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='date_of_registration',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='book',
            name='publishing_date',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='subject',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='date_of_registration',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='landline_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='mobile_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='person_in_charge',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='web_address',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='date_of_registration',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='file',
            name='opponent',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='subject',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='code',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_registration',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]