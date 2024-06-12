from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User


class ClientInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    organization_name = models.CharField(max_length = 50, blank=True, null=True )
    person_ident_number = models.CharField(_('personal identification number'),max_length = 255,blank=True, null=True)
    phone = models.CharField(max_length = 20,blank=True, null=True)

    def __str__(self):
        return str(self.phone)

    class Meta:
        verbose_name = _("Client of info")
        verbose_name_plural = _("Clients of info")