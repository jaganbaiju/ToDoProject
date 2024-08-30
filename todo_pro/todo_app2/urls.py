from django.urls import path
from . import views

app_name = 'task2'
urlpatterns = [
    path('', views.TaskListView.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/', views.TaskDetailView.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TaskDeleteView.as_view(), name='cbvdelete'),

]
