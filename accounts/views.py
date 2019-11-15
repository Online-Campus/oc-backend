from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, serializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from .models import Profile
from .serializers import ProfileSerializer

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication

class register_view(generics.CreateAPIView):
  permission_classes = (AllowAny,)

  queryset = Profile.objects.all()
  serializer_class = ProfileSerializer

class getUserView(APIView):
  authentication_classes = (JWTAuthentication,)
  permission_classes = (IsAuthenticated,)

  def get(self, request):
    user = ProfileSerializer(request.user)
    return Response({'current_user': user.data})    

class TokenObtainView(TokenObtainPairView):
  permission_classes = (AllowAny,)