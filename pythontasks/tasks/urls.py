from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='tasks-index'),
    path('about/', views.about, name='tasks-about'),
    path('<int:id_>/', views.task_details, name='tasks-task_details'),
    path('tags/', views.tags, name='tasks-tags_list'),
    # path('tags/<int:id_>/', views.tags_details, name='tasks-tag_details'),
]
