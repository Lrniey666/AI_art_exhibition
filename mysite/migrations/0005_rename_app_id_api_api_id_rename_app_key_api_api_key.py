# Generated by Django 4.2.1 on 2023-06-02 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0004_api"),
    ]

    operations = [
        migrations.RenameField(
            model_name="api",
            old_name="app_id",
            new_name="api_id",
        ),
        migrations.RenameField(
            model_name="api",
            old_name="app_key",
            new_name="api_key",
        ),
    ]
