<<<<<<< HEAD
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Notification


@login_required
def getNotification(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by('-date')
    old_notifications = notifications.filter(is_seen=True)
    new_notifications = notifications.filter(is_seen=False)

    response = render(request, 'notification.html', context={
        'old_notifications': old_notifications,
        'new_notifications': new_notifications
    })
    
    new_notifications.update(is_seen=True)

    return response
=======
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
>>>>>>> b158309b7d9a8b80440f548ef4b31cc0e730bfaa
