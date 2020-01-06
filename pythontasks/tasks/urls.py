from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='tasks-index'),
    path('about/', views.about, name='tasks-about'),
    path('task/<int:id_>/', views.task_details, name='tasks-task_details')
]
