from .models import Profile
from rest_framework import serializers

# Serializer for student user
class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = '__all__'
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    user = Profile.objects.create_user(**validated_data)
    return user

  def validate(self, data):
    print('VALIDATING')
    if data.first_name == '':
      return serializers.ValidationError('First name is a required field')
    if data.last_name == '':
      return serializers.ValidationError('Last name is a required field')
    return data

  def update(self, instance, validated_data):
    instance.first_name = validated_data.get('first_name', instance.first_name)
    instance.last_name = validated_data.get('last_name', instance.last_name)
    instance.birth_date = validated_data.get('birth_date', instance.birth_date)
    instance.bio = validated_data.get('bio', instance.bio)
    instance.save()
    return instance
