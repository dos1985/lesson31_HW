# Generated by Django 4.2 on 2023-05-21 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_options_user_total_ads"),
    ]

    operations = [
        migrations.AlterField(
            model_name="location",
            name="lat",
            field=models.DecimalField(
                blank=True, decimal_places=6, max_digits=8, null=True
            ),
        ),
        migrations.AlterField(
            model_name="location",
            name="lng",
            field=models.DecimalField(
                blank=True, decimal_places=6, max_digits=8, null=True
            ),
        ),
    ]
