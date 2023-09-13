from django.db import models
from api.validators import validate_string_fields


# Create your models here.
class Person(models.Model):
  name = models.CharField(max_length=255,
                          unique=True,
                          validators=[validate_string_fields])
  
  # Dynamic attributes
  # dynamic_attributes = models.JSONField(default=dict, null=True)

  def __str__(self) -> str:
    return self.name

  class Meta:
    # db_table = 'api_persons'
    indexes = [
      models.Index(fields=['name'])
    ]
