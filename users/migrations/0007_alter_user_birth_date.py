# Generated by Django 4.2 on 2023-06-09 06:51

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_alter_location_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birth_date",
            field=models.DateField(
                blank=True, null=True, validators=[users.validators.validate_birth_date]
            ),
        ),
    ]
