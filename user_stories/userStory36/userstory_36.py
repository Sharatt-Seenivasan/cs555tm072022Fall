import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date
import math

def listRecentDeaths(individuals):
    today = datetime.today()
    deathList = []
    for index, row in individuals.iterrows():
        if str(row['death']) != 'nan':
            deathDate = datetime.strptime(row['death']," %d %b %Y")
            if today.year == deathDate.year and (today-deathDate).days <= 30:
                deathList.append((row['id'], row['age']))
    print("US36: List of Recent Deaths:")
    print(deathList)
