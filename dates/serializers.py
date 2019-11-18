from rest_framework import serializers
from .models import Date

class DateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Date
    fields = '__all__'