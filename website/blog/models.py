from django.db import models
from django.utils.translation import ugettext_lazy as _

class Category(models.Model):
    name = models.CharField(_('name'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    public = models.BooleanField(_('public'), default=False)

    class Meta:
        verbose_name_plural = "categories"

    def __unicode__(self):
        return self.name
