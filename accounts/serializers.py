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