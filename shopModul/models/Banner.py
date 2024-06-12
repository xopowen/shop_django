from django.core import validators
from django.db import models
from django.db.models import ForeignKey
from django.utils.translation import gettext_lazy as _
from shopModul.models import Catalog
from shopModul.models.Manufacturer import Manufacturer


class Banner(models.Model):
    # панер произовдтеля
    # img - каринка банера
    # order - порядок показа в слайдоре
    order = models.IntegerField(null=True, blank=True,validators=[validators.MinValueValidator(0)])
    img = models.ImageField(null=True, blank=True,upload_to='img/banners/%Y/%m/%d/')
    catalog = ForeignKey(Catalog, on_delete=models.CASCADE)
    manufacturer = ForeignKey(Manufacturer, on_delete=models.CASCADE)
    head = models.CharField(max_length=255)
    subtitle = models.TextField(blank=True)

    def __str__(self):
        return f'Banner {self.manufacturer} for {self.catalog}'

    class Meta:
        verbose_name = _("Banner")
        verbose_name_plural = _("Banners")
