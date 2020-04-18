from django.contrib import admin
from .models import Venue, MyclubUser, Event


@admin.register(Venue)  # register custom ModelAdmin subclass (instead of admin.site.register(Venue, VenueAdmin))
class VenueAdmin(admin.ModelAdmin):
    fields = ('name', ('address', 'zip_code'), 'website', ('phone', 'email'))  # display some fields inline (edit form)
    list_display = ('name', 'address', 'website', 'phone')  # display fields in all items list
    ordering = ('name',)
    search_fields = ('name', 'address')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'venue', 'manager')  # displayed in all items list
    list_filter = ('name', 'date', 'venue')
    ordering = ('-date',)
    search_fields = ('name', 'venue')
    fieldsets = (
        ('Required Information', {'description': "These fields are required for each event",
                                  'fields': (('name', 'venue'), 'date')}),
        ('Optional Information', {'classes': ('expand',),  # to display optional section
                                  'fields': ('description', 'manager')}),
    )   # display fields in sections (edit form)


admin.site.register(MyclubUser)
