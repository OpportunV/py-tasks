from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='tasks-index'),
    path('about/', views.about, name='tasks-about'),
]
