from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
import tagging
from tagging.fields import TagField
from tagging.models import Tag

class Category(models.Model):
    name = models.CharField(_('name'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    public = models.BooleanField(_('public'), default=False)

    class Meta:
        verbose_name_plural = "categories"

    def __unicode__(self):
        return self.name

class Post(models.Model):
    DRAFT = 'D'
    PUBLISHED = 'P'
    REMOVED = 'R'
    STATE_CHOICES = (
        (DRAFT, _('Draft')),
        (PUBLISHED, _('Published')),
    )
    title = models.CharField(_('title'), max_length=100)
    category = models.ForeignKey(Category, verbose_name=_('category'), related_name="blog_posts")
    state = models.CharField(_('state'), max_length=1, choices=STATE_CHOICES, default=DRAFT)
    slug = models.SlugField(_('slug'), max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('author'), related_name="blog_posts")
    created_at = models.DateTimeField(_('created'), auto_now_add=True)
    published_at = models.DateTimeField(_('created'), blank=True, null=True, db_index=True)
    updated_at = models.DateTimeField(_('updated'), auto_now=True, db_index=True)
    body = models.TextField(_('body'))
    tags = TagField()

    def __unicode__(self):
        return self.title

    def is_published(self):
        return self.state == self.PUBLISHED

    def get_tags(self):
        return Tag.objects.get_for_object(self)

#tagging.register(Post)
