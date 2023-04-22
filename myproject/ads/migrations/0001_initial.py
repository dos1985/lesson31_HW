# Generated by Django 4.2 on 2023-04-20 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AdModel",
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
                ("name", models.CharField(max_length=50)),
                ("author", models.CharField(max_length=30)),
                ("address", models.CharField(max_length=120)),
                ("description", models.TextField(max_length=1000, null=True)),
                ("price", models.PositiveIntegerField()),
                ("is_published", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="CategoryModel",
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
                ("name", models.CharField(max_length=20)),
            ],
        ),
    ]
