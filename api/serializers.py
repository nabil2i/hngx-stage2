from api.validators import validate_string_fields
from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
  name = serializers.CharField(validators=[validate_string_fields])
  
  class Meta:
    model = Person
    fields = ['id', 'name']
  # id = serializers.IntegerField()
  # name = serializers.CharField(max_length=255)
  
  # override validation method
  def validate(self, data):
    name = data.get('name')
    
    data = super().validate(data)
    
    # Perform field-specific validation here
    if not isinstance(name, str):
      raise serializers.ValidationError('The field "name" must be a string.')
    if not name:
      raise serializers.ValidationError('Name is required.')
    
    return data
  
  # #override create method
  # def create(self, validated_data):
  #   person = Person(**validated_data)
  #   person.code = 1
  #   persone.save()
  #   return person