

from django.db import models
from django.contrib.auth.models import User

from shopModul.models import Product
from django.utils.translation import gettext_lazy as _


class Compare(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    class Meta:
        verbose_name = _('Compare')
        verbose_name_plural = _('Compare products')