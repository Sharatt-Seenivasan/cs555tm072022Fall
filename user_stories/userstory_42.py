from datetime import *
from dateutil.relativedelta import *


def reject_illegitimate_dates(date):
    date_format = " %d %b %Y"

    try:
        date_object = datetime.strptime(date, date_format)
        print(date_object)
    except:
        print ("Incorrect date format at <insert ID here>")

