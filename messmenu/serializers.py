from rest_framework import serializers
from .models import MessMenu

class MessMenuSerializer(serializers.ModelSerializer):
  class Meta:
    model = MessMenu
    fields = '__all__'