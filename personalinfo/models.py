from django.db import models

# Custom imports
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.api import APIField
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page


# Create your models here.
class personalinfo(Page):
    firstName = models.CharField(max_length=50, blank=False, null=True)
    lastName = models.CharField(max_length=50, blank=False, null=True)
    jobTitle = models.CharField(max_length=200, blank=False, null=True)
    description = RichTextField(blank=False, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    gitProfileLink = models.CharField(max_length=500, blank=True, null=True)
    gitApiLink = models.CharField(max_length=500, blank=True, null=True)
    linkedInLink = models.CharField(max_length=500, blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=False, null=True)
    location = models.CharField(max_length=50, blank=False, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('firstName'),
        FieldPanel('lastName'),
        FieldPanel('jobTitle'),
        FieldPanel('description'),
        FieldPanel('email'),
        FieldPanel('gitProfileLink'),
        FieldPanel('gitApiLink'),
        FieldPanel('linkedInLink'),
        FieldPanel('telephone'),
        FieldPanel('location'),
    ]

    api_fields = [
        APIField('firstName'),
        APIField('lastName'),
        APIField('jobTitle'),
        APIField('description'),
        APIField('email'),
        APIField('gitProfileLink'),
        APIField('gitApiLink'),
        APIField('linkedInLink'),
        APIField('telephone'),
        APIField('location'),
    ]

    max_count = 1
