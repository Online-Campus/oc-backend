from django.urls import path
from . import views

urlpatterns = [
  # Path to create a date list
  path('', views.DateView.as_view(), name='create-date-list'),

  # Path to retrieve and delete a date list
  path('<int:pk>', views.DateRetrieveView.as_view(), name='retrieve-delete-date')
]