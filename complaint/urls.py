from django.urls import path

from . import views

urlpatterns = [
    # Path to list all complaints
    path('', views.ListCreateComplaints.as_view(), name='complaint-list-view'),

    # Path to update a complaint
    path('update/<int:pk>', views.UpdateComplaintStatus.as_view(), name='update-complaint-status')
]
