from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register_view.as_view(), name='register-view'),
    path('token/obtain', views.TokenObtainView.as_view(), name='token-obtain-view'),
    path('current_user', views.getUpdateUserView.as_view(), name='get-current-user')
]
