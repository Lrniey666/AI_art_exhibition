# Generated by Django 4.2.1 on 2023-06-02 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0005_rename_app_id_api_api_id_rename_app_key_api_api_key"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="API",
            new_name="Tdx_api",
        ),
    ]
