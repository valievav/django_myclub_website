from django.shortcuts import render
from datetime import date
import calendar
from calendar import HTMLCalendar


def index(request, year=date.today().year, month=date.today().month):
    year = int(year)
    month = int(month)
    if year < 2000 or year > 2099:
        year = date.today().year
    month_str = calendar.month_name[month]
    title = f'Myclub Event Calendar - {month_str}, {year}'
    cal = HTMLCalendar().formatmonth(year, month)

    return render(request, 'events/calendar_base.html', {'title': title, 'cal': cal})  # returns HTML template
