from django.urls import path
from . import views
urlpatterns = [
  path('', views.DateView.as_view(), name='create-date-list'),
  path('<int:pk>', views.DateRetrieveView.as_view(), name='retrieve-delete-date')
]