from django.shortcuts import render

from rest_framework.response import Response 
from rest_framework import generics
from rest_framework.views import APIView

from .models import Leave
from .serializers import LeaveSerializer, LeaveUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class LeaveCreateListView(APIView):
  authentication_classes=(JWTAuthentication,)
  permission_classes=(IsAuthenticated,)

  def get(self, request):
    if request.user.account_type == "hostel_staff":
      listLeave = LeaveSerializer(Leave.objects.filter(status="submitted"), many=True)
      return Response(listLeave.data)

    if request.user.account_type == "student":
      listLeave = LeaveSerializer(Leave.objects.filter(owner=request.user), many=True)
      return Response(listLeave.data)

  def post(self, request):
    if request.user.account_type == "student":
      data = request.data
      user = request.user
      instance = LeaveSerializer(data = data)
      if instance.is_valid():
        obj = LeaveSerializer(instance.create(validated_data = instance.data, user = user))
        return Response({"status": 200, "message": "Leave created.", "data": obj.data})
      return Response({"status": 400, "message": "Error creating the object"})
    return Response({"message": "Only students can create leave applications."})


class LeaveUpdateView(generics.UpdateAPIView):
  authentication_classes=(JWTAuthentication,)
  permission_classes=(IsAuthenticated,)

  queryset = Leave.objects.all()
  serializer_class = LeaveUpdateSerializer