from django.urls import path

from . import views


app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
]
