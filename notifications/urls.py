from django.urls import path

from . import views

urlpatterns = [
    path('notifications/', views.getNotification, name="notification")
]
