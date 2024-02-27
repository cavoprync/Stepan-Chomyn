from django.urls import path

from . import views

urlpatterns = [
    path('model_list', views.models_list),
    path('post_list/', views.post_list)
    ]

