from rest_framework import serializers
from .models import Leave
from accounts.models import Profile
from accounts.serializers import ProfileSerializer

class LeaveSerializer(serializers.ModelSerializer):
  class Meta:
    model = Leave
    fields = '__all__'

  def create(self, validated_data, user):
    data = {**validated_data}
    data['owner'] = user
    instance = Leave.objects.create(**data)
    return instance

class LeaveUpdateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Leave
    fields = '__all__'
    extra_kwargs = {
      'owner': {'read_only': True},
      'reason': {'read_only': True},
      'start_date': {'read_only': True},
      'end_date': {'read_only': True},
      'created_at': {'read_only': True},
      'last_modified': {'read_only': True}
    }