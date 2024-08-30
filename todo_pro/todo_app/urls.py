from django.urls import path
from . import views

app_name = 'task'
urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:task_id>/', views.update, name='update'),
    path('delete/<int:task_id>/', views.delete, name='delete'),

]
