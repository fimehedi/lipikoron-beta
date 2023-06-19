from django import template

from ..models import Notification

register = template.Library()

@register.simple_tag
def unread_notification(user=None):
    if user.is_authenticated:
        return Notification.objects.filter(user=user, is_seen=False).count()
