from django.urls import path
from django_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form_alco/', views.create_alco, name='create_alco'),
    path('post_alco/', views.post_alco, name='post_alco')
]
