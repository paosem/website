from django.db import models
from django.utils.encoding import smart_str
from django.utils.translation import gettext_lazy as _

from core.models import Project

PUB_TYPES = (
    ("PA", _("Paper")),
    ("PR", _("Presentation")),
    ("TR", _("Training")),
    ("BO", _("Book")),
    ("VI", _("Video")),
)

# Create your models here.
class Journal(models.Model):
    """"""
    name = models.CharField(max_length=255, unique=True)
    url = models.URLField(null=True, blank=True)

    class Meta:
        db_table = 'journal'
        ordering = ['name']

    def __unicode__(self):
        return smart_str(f"{self.name}")

    def __str__(self):
        return self.__unicode__()

    def natural_key(self):
        return self.__unicode__()


class Publication(models.Model):
    """"""
    authors = models.TextField()
    title = models.TextField()
    abstract = models.TextField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    journal = models.ForeignKey(Journal, on_delete=models.PROTECT)
    volume = models.IntegerField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    doi = models.CharField(max_length=255)
    project = models.ManyToManyField(Project)
    euro_id = models.IntegerField()

    class Meta:
        db_table = 'publication'
        ordering = ['-year']

    def __unicode__(self):
        return smart_str(f"{self.title}")

    def __str__(self):
        return self.__unicode__()

    def natural_key(self):
        return self.__unicode__()

class PublicationExternal(models.Model):
    """"""
    authors = models.TextField()
    title = models.TextField()
    abstract = models.TextField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    journal = models.ForeignKey(Journal, on_delete=models.PROTECT)
    volume = models.IntegerField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    doi = models.CharField(max_length=255)
    project = models.ManyToManyField(Project)
    ttype = models.CharField(max_length=2, choices=PUB_TYPES)

    class Meta:
        db_table = 'publication_external'
        ordering = ['-year']

    def __unicode__(self):
        return smart_str(f"{self.title}")

    def __str__(self):
        return self.__unicode__()

    def natural_key(self):
        return self.__unicode__()
