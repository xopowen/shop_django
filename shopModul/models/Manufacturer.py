from django.db import models
from django.utils.translation import gettext_lazy as _



class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(null=True, blank=True,upload_to='img/manufacturer/%Y/%m/%d/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Manufacturer")
        verbose_name_plural = _('Manufacturers')