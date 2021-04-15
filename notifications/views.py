from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Notification


@login_required
def getNotification(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by('-date')

    return render(request, 'notification.html', context={
        'notifications': notifications
    })
