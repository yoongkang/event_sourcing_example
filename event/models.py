from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.postgres.fields import JSONField
from django.db import models


class Event(models.Model):
    """Event table that stores all model changes"""
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    object_id = models.PositiveIntegerField()
    time_created = models.DateTimeField()
    content_object = GenericForeignKey('content_type', 'object_id')
    body = JSONField()
