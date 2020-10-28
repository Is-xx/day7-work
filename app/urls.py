from django.urls import path
from app import views

urlpatterns = [
    path('user/<str:id>/', views.UserAPIView.as_view()),
    path('user/', views.UserAPIView.as_view()),
]