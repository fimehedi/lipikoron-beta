from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from .validators import CustomASCIIUsernameValidator


class Group(Group):
    pass


class CustomUser(AbstractUser):
    username_validator = CustomASCIIUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=50,
        unique=True,
        help_text=_('Required. 50 characters or fewer. Letters, digits and _ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    details         = models.TextField(max_length=150, blank=True)
    profile_picture = models.ImageField(upload_to='uploads/', blank=True)

    articles        = models.IntegerField(default=0)
    likes           = models.IntegerField(default=0)
    views           = models.IntegerField(default=0)
    balance         = models.IntegerField(default=0)
    verified        = models.BooleanField(default=False)
    is_lipikar      = models.BooleanField(default=False)

    def delete(self, *args, **kwargs):
        self.profile_picture.delete()
        super().delete(*args, **kwargs)




class Withdraw(models.Model):
    user    = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    withdraw_amount = models.IntegerField()

    METHOD_CHOICES = (
        ('bkash', 'BKash'),
        ('nagad', 'Nagad'),
        ('rocket', 'Rocket')
    )

    withdraw_method = models.CharField(
        max_length=10,
        choices=METHOD_CHOICES,
        default='bkash'
    )
    account_number = models.CharField(max_length=15)
    date           = models.DateField(auto_now_add=True)
    payment_done   = models.BooleanField(default=False)


    def __str__(self):
        if self.payment_done:
            return f"Payment Done for {self.user.get_full_name()} ({self.withdraw_amount} TK)"

        return f"Payment Request By {self.user.get_full_name()} ({self.withdraw_amount} TK)"



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
