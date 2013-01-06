from django.db import models
from django.utils.translation import ugettext_lazy as _

class PostCategory(models.Model):
    name = models.CharField(_('name'), max_length=50)
    description = models.TextField(_('description'), blank=True)

    def __unicode__(self):
        return self.name
