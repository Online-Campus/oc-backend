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