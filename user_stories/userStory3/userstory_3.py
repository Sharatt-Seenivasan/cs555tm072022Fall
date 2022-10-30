import pandas as pd
import parser
import math
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date

def compareDates(date_one, date_two):
  if datetime.strptime(date_one," %d %b %Y") > datetime.strptime(date_two," %d %b %Y"):
    return True
  return False

def birth_before_death(individuals_dataframe):
    df = individuals_dataframe
    for row in df.itertuples(index=False):
        if not type(row.death) == float or not math.isnan(row.death):
            if compareDates(row.birthday, row.death):
                print("ERROR: INDIVIDUAL: US03: " + row.id + ": " + "Died " + row.death + " before born " + row.birthday)
