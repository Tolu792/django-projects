from django.urls import path
from . import views

app_name = 'learning_logs'  # define the app_name

urlpatterns = [
    path('', views.main, name='main'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:id>', views.show_topic, name='show_topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:id>', views.new_entry, name='new_entry'),
    path('edit_entry/<int:id>', views.edit_entry, name='edit_entry'),
    path('delete_topic/<int:id>', views.delete_topic, name='delete_topic'),
    path('delete_entry/<int:id>', views.delete_entry, name='delete_entry'),
]
