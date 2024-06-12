from django.db import models

from django.utils.translation import gettext_lazy as _

class Question(models.Model):
    first_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=19)
    text = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    status_request = models.BooleanField(default=False)
    class Meta:
        ordering = ('date_time','-status_request')
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")