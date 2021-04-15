from django import template
from django.contrib.auth import get_user_model

register = template.Library()

@register.inclusion_tag('best_lipikar.html')
def best_lipikar(count=5):

    best_lipikar = get_user_model().objects.order_by('-likes', '-articles', '-views')

    return {
        "best_lipikar": best_lipikar[:count],

    }
