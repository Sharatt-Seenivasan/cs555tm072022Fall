import pytest
import pandas as pd
import pandas as pd
import io
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date
import user_stories
from user_stories import parents_not_too_old

def test_parents_not_too_old():
  
  person_details = [{'id': 'I2',
  'name': ' Steven /Brindley/',
  'gender': 'M',
  'birthday': ' 2 JUL 1969',
  'spouse': 'F2',
  'child': 'F3',
  'age': 83},{'id': 'I7',
  'name': ' Lisa /Rutherford/',
  'gender': 'F',
  'birthday': ' 5 MAR 1990',
  'spouse': 'F2',
  'age': 72},{'id': 'I8',
  'name': ' Reginald /Brindley/',
  'birthday': ' 10 AUG 2017',
  'child': 'F2',
  'age': 5},]
  family_details=[{'id': 'F2',
  'Husband ID': 'I2',
  'Husband Name': ' Steven /Brindley/',
  'Wife ID': 'I7',
  'Wife Name': ' Lisa /Rutherford/',
  'children': ['I8'],
  'married': ' 12 JUL 2016'},]
  
  strout= "ERROR:USERSTORY12 parents are too old"
  assert strout == parents_not_too_old(person_details,family_details)

