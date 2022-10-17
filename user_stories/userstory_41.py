from datetime import *
from dateutil.relativedelta import *

    
def include_partial_dates(date):
    listDate = date.split()
    if len(listDate) == 3:
        datetime_object = datetime.strptime(date, " %d %b %Y")
    if len(listDate) == 2:
        datetime_object = datetime.strptime(date, " %b %Y")
    if len(listDate) == 1:
        datetime_object = datetime.strptime(date, " %Y")
    
    print (datetime_object)
    return datetime_object

include_partial_dates(" 28 JUN 2018")