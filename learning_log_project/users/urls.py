from django.urls import path
from . import views

app_name = 'users'  # define the app_name

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('user-logout/', views.user_logout, name='user_logout')
]
