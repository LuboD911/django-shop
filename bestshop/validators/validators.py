from django import forms
from django.core.exceptions import ValidationError


def validate_dot_and_underscore(value):
    if '.' in value:
        raise forms.ValidationError("'.'is present in value. You can't have these symbols in the title. ")
    if '_' in value:
        raise forms.ValidationError("'_' is present in value. You can't have these symbols in the title. ")


def validate_price(value):
    if value < 10:
        raise ValidationError(f"The price must be at least 10$.")

def validate_rating(value):
    if value > 5:
        raise ValidationError(f"Maximum rating is 5")
    elif value < 1:
        raise ValidationError(f"Minimum rating is 1")