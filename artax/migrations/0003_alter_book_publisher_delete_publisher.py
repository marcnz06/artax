# Generated by Django 4.0.5 on 2023-05-28 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artax', '0002_book_lib_id_type_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(max_length=250),
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
    ]
