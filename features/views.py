from django.shortcuts import render, get_object_or_404
from . models import *

# Create your views here.
def getPage(request, slug):
    pageData = get_object_or_404(page, slug = slug)
    return render(request, 'page.html', {'page' : pageData})


def getEvents(request):
    eventData = event.objects.all()
    return render(request, 'events.html', {'event' : eventData})


def getLive(request):
    liveData = live.objects.all()
    return render(request, 'live.html', {'live' : liveData})


def getTeam(request):
    profile = teamProfile.objects.all()
    return render(request, 'team.html', {'profile' : profile})


def getMeme(request):
    memeData = meme.objects.all()
    return render(request, 'meme.html', {'meme' : memeData})


def comingSoon(request):
    return render(request, 'coming-soon.html')


def getActivity(request):
    quoteData = quote.objects.all()
    return render(request, "activity.html", {'quote' : quoteData})
