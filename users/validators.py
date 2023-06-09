from datetime import date

from django.core.exceptions import ValidationError


def validate_birth_date(value):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 9:
        raise ValidationError("Пользователь должен быть старше 9 лет.")


def validate_email_domain(value):
    if value.endswith('@rambler.ru'):
        raise ValidationError("Регистрация с почтового адреса в домене rambler.ru запрещена.")