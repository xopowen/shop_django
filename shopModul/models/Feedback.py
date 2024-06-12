from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


class Feedback(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    client = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    score = models.IntegerField(default=0, validators=[MaxValueValidator(10),MinValueValidator(0)])
    comment = models.TextField(max_length=255,null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Feedback ' + self.client.first_name
