from django.urls import path
from .views import MessMenuCreateView, MessMenuRUDView

urlpatterns = [
    path('', MessMenuCreateView.as_view(), name='create-mess-menu'),
    path('menu/<int:pk>', MessMenuRUDView.as_view(), name='rud-mess-menu')
]