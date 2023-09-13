from django.db import models

# Create your models here.
class Person(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self) -> str:
    return self.name

  class Meta:
    db_table = 'api_persons'
    indexes = [
      models.Index(fields=['name'])
    ]
