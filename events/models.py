from django.db import models

# Custom imports
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.api import APIField

# Create your models here.
class Events(Page):
        eventNameTwo = models.CharField(max_length=250, blank=False, null=True)
        eventFrom = models.CharField(max_length=10, blank=False, null=True)
        eventTo = models.CharField(max_length=10, blank=False, null=True)
        eventType = models.CharField(max_length=20, blank=False, null=True)
        eventDescription = RichTextField(blank=True,null=True)
        eventIcon = models.CharField(max_length=50, blank=False, null=True)

        content_panels = Page.content_panels + [
                FieldPanel('eventNameTwo'),
                FieldPanel('eventFrom'),
                FieldPanel('eventTo'),
                FieldPanel('eventType'),
                FieldPanel('eventDescription'),
                FieldPanel('eventIcon'),
        ]

        api_fields = [
                APIField('eventNameTwo'),
                APIField('eventFrom'),
                APIField('eventTo'),
                APIField('eventType'),
                APIField('eventDescription'),
                APIField('eventIcon'),
        ]