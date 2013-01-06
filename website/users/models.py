from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
import datetime
from django.utils.timezone import utc

class CustomUser(AbstractUser):
    mobile_phone = models.CharField(_('mobile phone'), max_length=20, blank=True)
    publish_mobile_phone = models.BooleanField(_('publish mobile phone'), default=False)
    home_phone = models.CharField(_('home phone'), max_length=20, blank=True)
    publish_home_phone = models.BooleanField(_('publish mobile phone'), default=False)
    ssh_public_key = models.TextField(_('public ssh key'), blank=True)
    date_left = models.DateTimeField(_('date left'),
        default = datetime.datetime.utcnow().replace(tzinfo=utc) + datetime.timedelta(days=10000))

