from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import MessMenu
from .serializers import MessMenuSerializer

class MessMenuCreateView(generics.ListCreateAPIView):
  permission_classes = (IsAuthenticated,)
  authentication_classes = (JWTAuthentication,)
  serializer_class = MessMenuSerializer
  queryset = MessMenu.objects.all()

class MessMenuRUDView(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsAuthenticated,)
  authentication_classes = (JWTAuthentication,)
  serializer_class = MessMenuSerializer
  queryset = MessMenu.objects.all()
