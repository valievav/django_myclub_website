from django.db import models


class Venue(models.Model):
    """
    Model for venues
    """
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField('Venue Address', max_length=300)
    zip_code = models.CharField('Venue Zip/Post Code', max_length=12)
    phone = models.CharField('Venue phone', max_length=20)
    website = models.URLField('Venue URL')
    email = models.EmailField('Venue Email')

    def __str__(self):
        return self.name


class MyclubUser(models.Model):
    """
    Model for Myclub users
    """
    first_name = models.CharField('Myclub user first name', max_length=30)
    last_name = models.CharField('Myclub user last name', max_length=30)
    email = models.EmailField('Myclub user email')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Event(models.Model):
    """
    Model for events
    """
    name = models.CharField('Event name', max_length=120)
    date = models.DateTimeField('Event date')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    manager = models.CharField('Event manager', max_length=120)
    attendees = models.ManyToManyField(MyclubUser)
    description = models.TextField('Event description', blank=True)

    def __str__(self):
        return self.name
