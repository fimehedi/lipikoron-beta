from django.urls import path, include

from . import views

from django.contrib.auth import urls

urlpatterns = [
    path("register", views.getRegister, name = "register"),
    path("settings", views.settings, name="settings"),
    path("account-delete", views.account_delete, name="account_delete"),





    path('', include('django.contrib.auth.urls')),


    # path("login", views.getLogin, name = "login"),
    # path("logout", views.getLogout, name = "logout"),
    # path("lipikar-form", views.becomeLipikar, name="lipikar_form"),
    # path('change-password/', views.UserPasswordChangeView.as_view(), name="change_password"),
    # path('password-reset/', views.UserPasswordResetView.as_view(), name="password_reset"),
    # path('password-reset-confirm/', views.UserPasswordResetView.as_view(), name="password_reset_confirm"),

]

