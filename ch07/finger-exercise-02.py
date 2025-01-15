# Finger exercise: Since 1958, Canadian Thanksgiving has occurred
# on the second Monday in October. Write a function that takes a year
# (>1957) as a parameter, and returns the number of days between
# Canadian Thanksgiving and Christmas.

import calendar

def canada_shopping_days(year):
    october = calendar.monthcalendar(year, calendar.OCTOBER)
    if october[0][calendar.MONDAY] != 0:
        thanksgiving = october[1][calendar.MONDAY]
    else:
        thanksgiving = october[2][calendar.MONDAY]
    _, october_length = calendar.monthrange(year, calendar.OCTOBER)
    _, november_length = calendar.monthrange(year, calendar.NOVEMBER)
    shopping_days = october_length - thanksgiving + november_length + 25
    return shopping_days