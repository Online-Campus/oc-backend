from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Complaint
from accounts.models import Profile
from .serializers import ComplaintSerializer, ComplaintUpdateSerializer
import json

# Create your views here.
class ListCreateComplaints(APIView):
  authentication_classes=(JWTAuthentication,)
  permission_classes=(IsAuthenticated,)
  def get(self, request):
    list = ComplaintSerializer(Complaint.objects.filter(owner = request.user), many=True)
    return Response(list.data)

  def post(self, request):
    data = request.data
    user = request.user
    instance = ComplaintSerializer(data = data)
    if instance.is_valid():
      obj = ComplaintSerializer(instance.create(validated_data = instance.data, user = user))
      return Response({'status': 200, 'message': 'Object created.', 'data': obj.data})
    return Response({'status': 400, 'message': 'Error creating the object'})

class UpdateComplaintStatus(UpdateAPIView):
  authentication_classes=(JWTAuthentication,)
  permission_classes=(IsAuthenticated,)
  queryset = Complaint.objects.all()

  serializer_class = ComplaintUpdateSerializer