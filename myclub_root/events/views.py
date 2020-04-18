from django.shortcuts import render
from datetime import date
import calendar
from calendar import HTMLCalendar
from django.http import HttpResponseRedirect
from .forms import VenueForm


def index(request, year=date.today().year, month=date.today().month):
    """
    Passes title and calendar to base.html template
    """
    year = int(year)
    month = int(month)
    if year < 2000 or year > 2099:
        year = date.today().year
    month_str = calendar.month_name[month]
    title = f'Myclub Event Calendar - {month_str}, {year}'
    cal = HTMLCalendar().formatmonth(year, month)

    return render(request, 'events/calendar_base.html', {'title': title, 'cal': cal})  # returns HTML template


def add_venue(request):
    """
    Passes 'add venue' form to the add_venue template
    """
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue/?submitted=True')
    else:
        form = VenueForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/add_venue.html', {'form': form,
                                                     'submitted': submitted})
