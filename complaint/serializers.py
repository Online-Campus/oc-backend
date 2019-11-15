from rest_framework import serializers

from .models import Complaint
from accounts.models import Profile
from accounts.serializers import ProfileSerializer

class ComplaintSerializer(serializers.ModelSerializer):
  class Meta:
    model = Complaint
    fields = '__all__'

  def create(self, validated_data, user):
    data = {**validated_data}
    data['owner'] = user
    instance = Complaint.objects.create(**data)
    return instance

class ComplaintUpdateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Complaint
    fields = '__all__'
    extra_kwargs = {'title': {'read_only': True}, 'owner': {'read_only': True}, 'description': {'read_only': True}}