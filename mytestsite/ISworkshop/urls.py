from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='profilepage'),
    path('forms/', views.form, name='profilepageforms'),
]

