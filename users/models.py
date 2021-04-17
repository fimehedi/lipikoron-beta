from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .validators import CustomASCIIUsernameValidator

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