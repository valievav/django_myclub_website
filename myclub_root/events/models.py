from django.db import models
from django.contrib.auth.models import User


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField('Venue Address', max_length=300)
    zip_code = models.CharField('Venue Zip/Post Code', max_length=12, blank=True)
    phone = models.CharField('Venue phone', max_length=20, blank=True)   # blank=True for optional field
    website = models.URLField('Venue URL', blank=True)
    email = models.EmailField('Venue Email', blank=True)

    def __str__(self):
        return self.name


class MyclubUser(models.Model):
    first_name = models.CharField('Myclub user first name', max_length=30)
    last_name = models.CharField('Myclub user last name', max_length=30)
    email = models.EmailField('Myclub user email')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Event(models.Model):
    name = models.CharField('Event name', max_length=120)
    date = models.DateTimeField('Event date')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, blank=True, on_delete=models.SET_NULL, null=True)
    attendees = models.ManyToManyField(MyclubUser)
    description = models.TextField('Event description', blank=True)

    def __str__(self):
        return self.name
