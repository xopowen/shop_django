from django.db import models
from django.utils.translation import gettext_lazy as _




class Catalog(models.Model):
    name = models.CharField(max_length=255,unique=True)
    img = models.ImageField(blank=True,null=True,upload_to='img/catalog/%Y/%m/%d/')
    order = models.IntegerField(unique=True)
    # property = GenericRelation(Property)
    def __str__(self):
        return self.name
    class Meta:
      verbose_name = _("Catalog")
      verbose_name_plural = _("Catalogs")


