import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date
import math

def listUpComingBirthdays(individuals):
    today = datetime.today()
    birthdayList = []
    for index, row in individuals.iterrows():
        if str(row['birthday']) != 'nan':
            birthday = datetime.strptime(row['birthday']," %d %b %Y")
            birthDate = datetime(today.year, birthday.month, birthday.day)
            if abs((today-birthDate).days) <= 30:
                birthdayList.append((row['id'],row['age']))
    print("US38: List of Upcoming Birthdays:")
    print(birthdayList)
