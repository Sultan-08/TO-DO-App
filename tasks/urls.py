from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.TaskListView.as_view(), name='index'),            # CBV - list
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='detail'), # CBV - detail
    path('task/add/', views.create_task, name='add'),               # FBV - create
    path('task/<int:pk>/edit/', views.edit_task, name='edit'),     # FBV - edit
    path('task/<int:pk>/delete/', views.delete_task, name='delete'), # FBV - delete
    path('task/<int:pk>/toggle/', views.toggle_complete, name='toggle'), # FBV - toggle complete
]
