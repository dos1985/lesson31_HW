# Generated by Django 4.2 on 2023-06-06 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0004_categorymodel_slug_alter_admodel_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="admodel",
            name="is_published",
            field=models.BooleanField(default=False),
        ),
    ]