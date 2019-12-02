from django.urls import path
from .views import MessMenuCreateView, MessMenuRUDView

urlpatterns = [
    # Path to create a new mess menu
    path('', MessMenuCreateView.as_view(), name='create-mess-menu'),

    # Path to retrieve, update or delete mess menu
    path('menu/<int:pk>', MessMenuRUDView.as_view(), name='rud-mess-menu')
]