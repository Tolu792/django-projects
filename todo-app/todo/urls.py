from django.urls import path
from . import views

app_name = 'todo'  # define the app name

urlpatterns = [
    path('', views.main, name='main'),
    path('remove/<int:id>', views.remove, name='remove'),
]
