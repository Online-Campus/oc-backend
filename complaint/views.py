from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Complaint
from .serializers import ComplaintSerializer
import json

# Create your views here.
class ListCreateComplaints(APIView):
  authentication_classes=(JWTAuthentication,)
  permission_classes=(IsAuthenticated,)
  def get(self, request):
    list = ComplaintSerializer(Complaint.objects.filter(owner = request.user), many=True)
    return Response(list.data)

  def post(self, request):
    return HttpResponse('Create complaint...')