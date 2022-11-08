import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date
import math

def listRecentDeaths(individuals):
    current= datetime.now()
    recentdeathlist=[]
    for index,row in individuals.iterrows():
        if not type(row.death)==float or not math.isnan(row.death):
            deathDay= datetime.strptime(row.death," %d %b %Y")
            if (current.year - deathDay.year == 0 ):
                if ((current - deathDay).days < 30):
                    name=row["name"].strip("/")
                    deathdate= str(row["death"])
                    recentdeathlist.append("US:36 List of recent deaths: "+name +" "+str(deathdate))
    return recentdeathlist

