from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Profile
from .serializers import ProfileSerializer

from rest_framework_simplejwt.views import TokenObtainPairView

class register_view(generics.CreateAPIView):
  permission_classes = (AllowAny,)

  queryset = Profile.objects.all()
  serializer_class = ProfileSerializer

class TokenObtainView(TokenObtainPairView):
  permission_classes = (AllowAny,)