from django.urls import path
from . import views

urlpatterns = [
    path("page/<slug:slug>", views.getPage, name = "page"),
    path('events', views.getEvents, name = 'events'),
    path('lives', views.getLive, name = 'lives'),
    path('team', views.getTeam, name = 'team'),
    path('memes', views.getMeme, name = 'memes'),
    path('activity', views.getActivity, name = 'activity'),
    path('coming-soon', views.comingSoon, name = 'coming-soon')
]
