from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import FileExtensionValidator
from django.db import models


class Document(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='documents/%Y/%m/%d/',
                            validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])])
    show_page = models.BooleanField(default=False)

    def __str__(self):
        return F'{self.name} show page -> {self.show_page}'
