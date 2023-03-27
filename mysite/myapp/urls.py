from django.urls import path
from .views import views, sbom_main

urlpatterns = [
    path('', views.index, name='index'),
    path('jobs/', views.submit_repo_for_scan, name='submit_repo_for_scan'),
    path('submit/', sbom_main.user_input, name='user_input'),
]