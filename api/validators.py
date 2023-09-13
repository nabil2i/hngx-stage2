from django.core.exceptions import ValidationError

def validate_string_fields(field):
  """Field must be a string"""
  if not isinstance(field, str):
    raise ValidationError(f'The field "{field}" must be a string.')
