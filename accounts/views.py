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

class getUpdateUserView(generics.RetrieveUpdateAPIView):
  authentication_classes = (JWTAuthentication,)
  permission_classes = (IsAuthenticated,)

  def get(self, request):
    user = ProfileSerializer(request.user)
    return Response({'current_user': user.data})

  def post(self, request):
    current_user = Profile.objects.get(username=request.user.username)
    if 'bio' in request.data and request.data['bio'] != '':
      current_user.bio = request.data['bio']

    if 'first_name' in request.data and request.data['first_name'] != '':
      current_user.first_name = request.data['first_name']

    if 'last_name' in request.data and request.data['last_name'] != '':
      current_user.last_name = request.data['last_name']

    if 'birth_date' in request.data and request.data['birth_date'] != '':
      current_user.birth_date = request.data['birth_date']

    if 'contact_no' in request.data and request.data['contact_no'] != '':
      current_user.contact_no = request.data['contact_no']

    current_user.save()
    user = ProfileSerializer(current_user)
    return Response({'current_user': user.data})

class TokenObtainView(TokenObtainPairView):
  permission_classes = (AllowAny,)

class VerifyAccount(APIView):
  permission_classes = (AllowAny,)

  def get(self, request, pk):
    profile = Profile.objects.get(pk=pk)
    profile.is_verified = True
    profile.save()
    return HttpResponse("Your account is now verified!")