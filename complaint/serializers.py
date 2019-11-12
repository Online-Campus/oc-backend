from rest_framework import serializers

from .models import Complaint
from accounts.models import Profile

class ComplaintSerializer(serializers.ModelSerializer):
  class Meta:
    model = Complaint
    fields = '__all__'

  def create(self, validated_data, user):
    complaint = Complaint.save(owner = user, **validated_data)
    return complaint