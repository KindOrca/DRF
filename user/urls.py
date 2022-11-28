from django.urls import path, include
from user.views import RegisterAPIView, AuthView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns =[
    path('signup/', RegisterAPIView.as_view()),
    path("auth/", AuthView.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view()),
]