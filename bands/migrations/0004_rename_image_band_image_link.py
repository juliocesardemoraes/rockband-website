# Generated by Django 4.2.1 on 2023-06-07 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bands", "0003_remove_band_formed_in_remove_band_genre_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="band",
            old_name="image",
            new_name="image_link",
        ),
    ]
