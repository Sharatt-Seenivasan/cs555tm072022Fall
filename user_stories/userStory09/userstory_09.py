import io
import unittest
import unittest.mock
import pandas as pd
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date

def greaterDate(first_date, second_date):
    if datetime.strptime(first_date, " %d %b %Y") > datetime.strptime(second_date, " %d %b %Y"):
        return True
    return False

def areBirthsBeforeParentDeaths(individuals_dataframe, family_dataframe, family_id_indices):
  for index, row in family_dataframe.iterrows():
    husband_death = individuals_dataframe.loc[individuals_dataframe['id'] == row['Husband ID'], 'death'].iloc[0]
    wife_death = individuals_dataframe.loc[individuals_dataframe['id'] == row['Wife ID'], 'death'].iloc[0]
    if(str(row['children'])!='nan'):
      for child_id in row['children']:
        child_birthday = individuals_dataframe.loc[individuals_dataframe['id'] == child_id, 'birthday'].iloc[0]
        if str(child_birthday) != 'nan':
          if str(husband_death) != 'nan' and greaterDate(str(child_birthday),str(husband_death)):
            print("ERROR: FAMILY: US09: Input Line # " + str(family_id_indices[row['id']]) + " Husband " + row['Husband ID'] + " in Family " + row['id'] + " dies before Child " + child_id + " is born.")
          if str(wife_death) != 'nan' and greaterDate(str(child_birthday),str(wife_death)):
            print("ERROR: FAMILY: US09: Input Line # " + str(family_id_indices[row['id']]) + " Wife " + row['Wife ID'] + " in Family " + row['id'] + " dies before Child " + child_id + " is born.")
