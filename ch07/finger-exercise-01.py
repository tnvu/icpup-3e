# Finger exercise: Write a function that meets the specification
# def shopping_days(year):
# """year a number >= 1941
#    Returns the number of days between U.S. Thanksgiving and
#    Christmas in year"""

import calendar

def shopping_days(year):
    november = calendar.monthcalendar(year, calendar.NOVEMBER)
    if november[0][calendar.THURSDAY] != 0:
        thanksgiving = november[3][calendar.THURSDAY]
    else:
        thanksgiving = november[4][calendar.THURSDAY]
    _, november_length = calendar.monthrange(year, calendar.NOVEMBER)
    shopping_days = november_length - thanksgiving + 25
    return shopping_days