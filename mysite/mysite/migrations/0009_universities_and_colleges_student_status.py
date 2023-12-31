# Generated by Django 4.2.1 on 2023-06-03 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0008_alter_household_income_year"),
    ]

    operations = [
        migrations.CreateModel(
            name="Universities_and_colleges_Student_status",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("year", models.CharField(max_length=255)),
                ("city_name", models.CharField(max_length=255)),
                ("county_code", models.CharField(max_length=255)),
                ("type", models.CharField(max_length=255)),
                ("SchoolCode", models.CharField(max_length=255)),
                ("SchoolName", models.CharField(max_length=255)),
                ("NumberOfMales", models.CharField(max_length=255)),
                ("NumberOfFemales", models.CharField(max_length=255)),
                ("Total", models.CharField(max_length=255)),
            ],
        ),
    ]
