# Generated by Django 4.0.5 on 2023-06-04 08:01

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('artax', '0007_client_address_alter_book_date_of_registration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='landline_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region='LB'),
        ),
        migrations.AlterField(
            model_name='client',
            name='mobile_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
    ]
