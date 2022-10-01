from datetime import datetime
from datetime import date

def isDateBeforeCurrentDate(event_date):
  if date.today() > event_date.date():
    return True
  return False