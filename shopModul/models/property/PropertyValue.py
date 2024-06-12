
from django.db import models

from django.utils.translation import gettext_lazy as _



class PropertyValue(models.Model):

    property = models.ForeignKey('Property', on_delete=models.CASCADE,null=True)
    value = models.CharField(max_length=255,default='',unique=True)

    show_menu = models.BooleanField(default=False)
    show_popup = models.BooleanField(default=False)
    show_filter = models.BooleanField(default=False)
    selected = models.BooleanField()
    def __str__(self):
        return F'Property:{self.property} -> {self.value}'

    class Meta:
        verbose_name = _("Value of Propert")
        verbose_name_plural = _("Values of Property")