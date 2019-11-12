from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class ListCreateComplaints(APIView):
  authentication_classes=(JWTAuthentication,)
  permission_classes=(IsAuthenticated,)
  def get(self, request):
    print(request.user)
    return HttpResponse('Complaint module')