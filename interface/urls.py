from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="interface-home"),
    path('progress/', views.progress, name='interface-progress'),
    path('rewards/', views.rewards, name='interface-rewards')
]
