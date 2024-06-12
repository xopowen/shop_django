from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericRelation

from shopModul.models import ImgLink


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    img_face = models.ImageField(upload_to='img/events/%Y/%m/%d/')
    address = models.TextField()
    img = GenericRelation(ImgLink,null=True,blank=True)
    time_start = models.DateTimeField()
    def __str__(self):
        return F"{self.name}->{self.time_start.date()}:{self.time_start.time()}"
    class Meta:
        ordering = ('-time_start',)
        verbose_name = _('Event')
        verbose_name_plural = _('Events')