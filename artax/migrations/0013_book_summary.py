# Generated by Django 4.2.4 on 2023-08-13 13:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("artax", "0012_language_book_language"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="summary",
            field=models.ImageField(blank=True, null=True, upload_to="summaries"),
        ),
    ]