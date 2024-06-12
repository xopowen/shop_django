from django.db import models
from django.utils.translation import gettext_lazy as _

class Organization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Organization")
        verbose_name_plural = _("Organizations")