from django.urls import path
from . import views

#URLConfigurations

urlpatterns = [
    path('sample/', views.sample)
]