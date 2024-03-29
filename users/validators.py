import re

from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class CustomASCIIUsernameValidator(validators.RegexValidator):
    regex = r'^[A-Za-z0-9_]+$'
    message = _(
        'Enter a valid username. This value may contain only English letters, '
        'numbers, and _ characters.'
    )
    flags = re.ASCII


@deconstructible
class CustomUnicodeUsernameValidator(validators.RegexValidator):
    regex = r'^[\w.@+-]+\Z'
    message = _(
        'Enter a valid username. This value may contain only letters, '
        'numbers, and @/./+/-/_ characters.'
    )
    flags = 0
