from django.shortcuts import render
from django.http import HttpResponse
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

    return HttpResponse(f'<h1>{title}</h1>'
                        f'<p>{cal}</p>')
