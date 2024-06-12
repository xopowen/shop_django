from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import gettext_lazy as _
from shopModul.models import  Feedback


class News(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(blank=True,null=True,upload_to='img/news/%Y/%m/%d/')
    author = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    feedback = GenericRelation(Feedback)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("A news")
        verbose_name_plural = _("News")