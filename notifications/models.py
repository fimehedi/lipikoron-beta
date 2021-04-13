from django.db import models
from django.contrib.auth import get_user_model


class Notification(models.Model):
    NOTIFICATION_TYPES  = ((1, 'Like'), (2, 'Comment'))

    post                = models.ForeignKey('blog.article', on_delete=models.CASCADE, blank=True, related_name='notify_post')
    user                = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='notify_user')
    sender              = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='notify_sender')
    notification_type   = models.IntegerField(choices=NOTIFICATION_TYPES)
    notification_text   = models.CharField(max_length=100, blank=True)
    date                = models.DateTimeField(auto_now_add=True)
    is_seen             = models.BooleanField(default=False)


    def __str__(self):
        status = None

        if self.notification_type == 1:
            status = 'Liked'
        elif self.notification_type == 2:
            status = 'Commented'

        return f"{self.sender.get_full_name()} {status} '{self.post}'"


