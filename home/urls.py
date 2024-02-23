from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.home_about),
    path('projects/', views.home_projects),
    path('projects/<int:id>/', views.projects),
]
