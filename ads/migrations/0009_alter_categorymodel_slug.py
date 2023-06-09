# Generated by Django 4.2.2 on 2023-06-12 08:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0008_alter_categorymodel_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categorymodel",
            name="slug",
            field=models.CharField(
                unique=True,
                validators=[
                    django.core.validators.MinLengthValidator(5),
                    django.core.validators.MaxLengthValidator(10),
                ],
            ),
        ),
    ]
