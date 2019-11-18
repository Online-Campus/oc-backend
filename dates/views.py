from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import DateSerializer
from .models import Date

class DateView(generics.CreateAPIView):
  permission_classes = (IsAuthenticated,)
  authentication_classes = (JWTAuthentication,)

  queryset = Date.objects.all()
  serializer_class = DateSerializer

class DateRetrieveView(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsAuthenticated,)
  authentication_classes = (JWTAuthentication,)

  queryset = Date.objects.all()
  serializer_class = DateSerializer