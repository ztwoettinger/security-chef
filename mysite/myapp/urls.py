from django.urls import path
from .views import new_page, views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_page/', new_page.render_new_page, name='new_page'),
]