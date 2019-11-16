from django.urls import path
from . import views

urlpatterns = [
  path('', views.LeaveCreateListView.as_view(), name='create-list-leaves'),
  path('update/<int:pk>', views.LeaveUpdateView.as_view(), name='update-leaves')
]