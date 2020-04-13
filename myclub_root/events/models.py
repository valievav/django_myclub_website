from django.db import models


class Events(models.Model):
    """
    Model for events
    """
    name = models.CharField(verbose_name='Event name', max_length=120)
    date = models.DateTimeField(verbose_name='Event date')
    venue = models.CharField(verbose_name='Event venue', max_length=120)
    manager = models.CharField(verbose_name='Event manager', max_length=120)
    description = models.TextField(verbose_name='Event description', blank=True)  # can be empty

