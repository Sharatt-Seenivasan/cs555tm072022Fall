import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date
import math

def listUpComingBirthdays(individuals):
    current= datetime.now()
    upcomingbirthdays=[]
    for index,row in individuals.iterrows():
        if not type(row.birthday)==float or not math.isnan(row.birthday):
            birthday= datetime.strptime(row.birthday," %d %b %Y")
            if ((birthday.month-current.month) ==0 or (birthday.month-current.month)==1 ):
                if((birthday.day-current.day)<30):
                    name=''.join(row["name"].split('/'))
                    age=row["age"]
                    birthday= str(row["birthday"])
                    upcomingbirthdays.append("US:38 List of upcoming birthdays:" +name +" : "+ "age:"+str(age) +str(birthday))
                    print(upcomingbirthdays)
    return upcomingbirthdays 

