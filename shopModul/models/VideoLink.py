from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import FileExtensionValidator
from django.db import models


class VideoLink(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    link = models.FileField(upload_to='move/%Y/%m/%d/', validators=[
        FileExtensionValidator(['mp3', 'wav', 'mp4', 'webm'])])

    def __str__(self):
        return self.link.path