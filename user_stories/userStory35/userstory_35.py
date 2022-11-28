import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date
import math

def listRecentBirths(individuals):
    current = datetime.now()
    recentBirthsList = []
    for index,row in individuals.iterrows():
        if not type(row.birthday) == float or not math.isnan(row.birthday):
            birthday = datetime.strptime(row.birthday, " %d %b %Y")
            if (current.year - birthday.year == 0):
                if ((current - birthday).days < 30):
                    name = row["name"].strip("/")
                    birthDate = str(row["birthday"])
                    recentBirthsList.append((row['id'],row['age']))
    print("US35: List of recent births: ")
    print(recentBirthsList)