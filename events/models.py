from django.db import models
from django import forms

# Custom imports
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.api import APIField

# Create your models here.
class Events(Page):
        class EventType(models.TextChoices):
                FULLTIME = "Full-time"
                PARTTIME = "Part-time"
                APPRENTICESHIP = "Apprenticeship"
                SHADOWING = "Shadowing"

        eventNameTwo = models.CharField(max_length=250, blank=False, null=True)
        eventFrom = models.DateField(blank=False, null=True)
        eventTo = models.DateField(blank=True, null=True)
        eventType = models.TextField(choices=EventType.choices, default=EventType.FULLTIME)
        eventDescription = RichTextField(blank=True,null=True)
        eventIcon = models.CharField(max_length=50, blank=False, null=True)

        content_panels = Page.content_panels + [
                FieldPanel('eventNameTwo'),
                FieldPanel('eventFrom'),
                FieldPanel('eventTo'),
                FieldPanel('eventType', widget=forms.Select),
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