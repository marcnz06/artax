# Generated by Django 4.0.5 on 2023-06-07 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artax', '0009_alter_client_mobile_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='location',
        ),
        migrations.AddField(
            model_name='book',
            name='locations',
            field=models.ManyToManyField(related_name='books', to='artax.location'),
        ),
    ]