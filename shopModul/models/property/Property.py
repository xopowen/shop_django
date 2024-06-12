
from django.db import models




class Property(models.Model):
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    # object_id = models.PositiveIntegerField(null=True, blank=True)
    # content_object = GenericForeignKey('content_type', 'object_id')
    catalog = models.ForeignKey('Catalog',on_delete=models.CASCADE, blank=True, null=True)
    # filter = ForeignKey(Filter, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50)
    show_popup = models.BooleanField(default=False)
    show_filter = models.BooleanField(default=False)
    selected = models.BooleanField()
    # class Meta:
    #     verbose_name = _("Property")
    #     verbose_name_plural = _("Properties")

    def __str__(self):
        return self.name


