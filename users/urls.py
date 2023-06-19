from django.urls import path, include

from . import views

urlpatterns = [
    path("register/", views.getRegister, name = "register"),
    path("settings/", views.settings, name="settings"),
    path("account-delete/", views.account_delete, name="account_delete"),

    path('', include('django.contrib.auth.urls')),

    path("balance/", views.getBalance, name="balance"),
    path("withdraw/", views.getWithdraw, name="withdraw"),
    path('notifications/', views.getNotification, name="notification"),

]

