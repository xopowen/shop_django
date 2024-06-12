from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class ImgLink(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    link = models.ImageField(blank=True, null=True, upload_to='img/img/%Y/%m/%d/')
    # linkImgWepb = models.ImageField(blank=True, null=True, upload_to='/img/%Y/%m/%d/')

    def __str__(self):
        return self.link.path

