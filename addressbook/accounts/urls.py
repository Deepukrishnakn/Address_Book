from . import views
from django.urls import path
from .views import LoginAPIView, UserAPIView,LogoutAPIView,RefreshAPIView

urlpatterns = [
    # path('register',RegisterAPIView.as_view()),
    path('register/', views.registeruser, name="registeruser"),
    path('Login/',LoginAPIView.as_view()),
    path('user/',UserAPIView.as_view()),
    path('logout/',LogoutAPIView.as_view()),
    path('refresh/',RefreshAPIView.as_view(), name="refresh"),

]