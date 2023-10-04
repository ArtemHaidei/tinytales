from marshmallow import ValidationError


def validate_password(value):
    if not any(char.isdigit() for char in value):
        raise ValidationError("ПThe password must contain at least one digit.")
    if not any(char.isalpha() for char in value):
        raise ValidationError("The password must contain at least one letter.")
    if len(value) < 8:
        raise ValidationError("The password must contain at least 8 characters.")