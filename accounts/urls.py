from django.urls import path

from . import views

urlpatterns = [
    # Path to create new user
    path('register', views.register_view.as_view(), name='register-view'),

    # Path to obtain a token
    path('token/obtain', views.TokenObtainView.as_view(), name='token-obtain-view'),

    # Path to fetch details of current user
    path('current_user', views.getUpdateUserView.as_view(), name='get-current-user'),

    # Path to verify token
    path('verify/<int:pk>', views.VerifyAccount.as_view(), name='verify-account')
]
