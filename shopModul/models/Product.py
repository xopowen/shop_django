
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import gettext_lazy as _


from shopModul.models import Document, Manufacturer, Catalog, \
    Proportion, Feedback, ImgLink, VideoLink


class Product(models.Model):

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255,null=True,blank=True)

    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True)
    catalog = models.ForeignKey(Catalog, on_delete=models.SET_NULL, null=True)

    documents = GenericRelation(Document, null=True, blank=True)

    act = models.IntegerField(null=True, blank=True)
    amt = models.IntegerField(default=0)

    price = models.FloatField(null=True, blank=True)
    old_price = models.FloatField(null=True, blank=True)
    currency = models.CharField(choices=(('₽', '₽'), ('$', '$')), max_length=1,null=True,blank=True)

    img = GenericRelation(ImgLink, null=True, blank=True)
    video = GenericRelation(VideoLink, null=True, blank=True)

    technical_feature = models.TextField(null=True, blank=True)
    article = models.CharField(max_length=12 ,default="000 000")

    YTP = models.CharField(max_length=20, null=True, blank=True)

    proportion = GenericRelation(Proportion, null=True, blank=True)
    feedback = GenericRelation(Feedback)

    date = models.DateTimeField(auto_now_add=True)

    visibility = models.BooleanField(default=False)

    def __str__(self):
        return F"{self.name} :catalog:{self.catalog}; date:{self.date}"

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _('Products')