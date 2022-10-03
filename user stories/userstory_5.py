#User Story 5

from datetime import datetime
from datetime import date
import pandas as pd
from dateutil.relativedelta import relativedelta
import math

def greaterDate(first_date, second_date):
    if datetime.strptime(first_date, " %d %b %Y") > datetime.strptime(second_date, " %d %b %Y"):
        return True
    return False

def marriageBeforeDeath(individuals, families):
    for index, row in families.iterrows():
        marriageDate = row['married']
        husband_death = individuals.loc[individuals['id'] == row['Husband ID'], 'death'].iloc[0]
        wife_death = individuals.loc[individuals['id'] == row['Wife ID'], 'death'].iloc[0]

        if greaterDate(husband_death, marriageDate) == False:
            print("ERROR: Husband death date before marriage.")

        if greaterDate(wife_death, marriageDate) == False:
            print("Error: Wife death date before marriage.")
