from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListCreateComplaints.as_view(), name='complaint-list-view')
]
