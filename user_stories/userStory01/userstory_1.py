import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date

def isDateBeforeCurrentDate(event_date):
  return date.today() > event_date.date()

def createIndDataframe(filename):
  individuals = []
  individuals_id_and_name = {}
  f = open(filename, "r")
  lines = f.readlines()

  indices = []
  for i in range(0,len(lines)):
    line = lines[i]
    level = line[0]
    if 'INDI' in line.split() and level == '0':
      indices.append(i)

  for i in indices:
    is_dead = False
    person = {
    }
    if indices.index(i) != len(indices)-1:
      for j in range(i,indices[indices.index(i)+1]):
        line = lines[j]
        level = line[0]
        if 'INDI' in line.split() and level == '0':
          person['id'] = line.split()[1].replace('@','')
        if 'NAME' in line.split():
          person['name'] = line.split('NAME')[1].replace('\n','')
          individuals_id_and_name[person['id']] = person['name']
        if 'SEX' in line.split() and level == '1':
          person['gender'] = line.split()[2]
        if 'BIRT' in line.split():
          person['birthday'] =  lines[j+1].split('DATE')[1].replace('\n','')
        if 'DEAT' in line.split():
          is_dead = True
          person['death'] = lines[j+1].split('DATE')[1].replace('\n','')
        if 'FAMC' in line.split():
          person['child'] = line.split()[2].replace('@','')
        if 'FAMS' in line.split():
          person['spouse'] = line.split()[2].replace('@','')
    else:
      for j in range(i,len(lines)-1):
        line = lines[j]
        level = line[0]
        if 'INDI' in line.split() and level == '0':
          person['id'] = line.split()[1].replace('@','')
        if 'NAME' in line.split():
          person['name'] = line.split('NAME')[1].replace('\n','')
          individuals_id_and_name[person['id']] = person['name']
        if 'SEX' in line.split() and level == '1':
          person['gender'] = line.split()[2]
        if 'BIRT' in line.split():
          person['birthday'] = lines[j+1].split('DATE')[1].replace('\n','')
        if 'DEAT' in line.split():
          is_dead = True
          person['death'] = lines[j+1].split('DATE')[1].replace('\n','')
        if 'FAMC' in line.split():
          person['child'] = line.split()[2].replace('@','')
        if 'FAMS' in line.split():
          person['spouse'] = line.split()[2].replace('@','')

    if is_dead:
       person['alive'] = False
       person['age'] = relativedelta(datetime.strptime(person['death']," %d %b %Y"),datetime.strptime(person['birthday']," %d %b %Y")).years
    else:
      person['alive'] = True
      today = date.today()
      person['age'] = relativedelta(today, datetime.strptime(person['birthday']," %d %b %Y")).years

    individuals.append(person)
      
  return (pd.DataFrame(individuals),individuals_id_and_name)

def createFamilyDataframe(filename, individuals_id_and_name):
  families = []
  f = open(filename, "r")
  lines = f.readlines()

  indices = []
  for i in range(0,len(lines)):
    line = lines[i]
    level = line[0]
    if 'FAM' in line.split() and level == '0':
      indices.append(i)
  
  for i in indices:
    family = {
    }
    if indices.index(i) != len(indices)-1:
      for j in range(i,indices[indices.index(i)+1]):
        line = lines[j]
        level = line[0]
        if 'FAM' in line.split() and level == '0':
          family['id'] = line.split()[1].replace('@','')
        if 'MARR' in line.split():
          family['married'] = lines[j+1].split('DATE')[1].replace('\n','')
        if 'DIV' in line.split():
          family['divorced'] = lines[j+1].split('DATE')[1].replace('\n','')
        if 'HUSB' in line.split():
          family['Husband ID'] = line.split()[2].replace('@','')
          family['Husband Name'] = individuals_id_and_name[family['Husband ID']]
        if 'WIFE' in line.split():
          family['Wife ID'] = line.split()[2].replace('@','')
          family['Wife Name'] = individuals_id_and_name[family['Wife ID']]
        if 'CHIL' in line.split():
          if 'children' in family: 
            family['children'].append(line.split()[2].replace('@',''))
          else:
            family['children'] = []
            family['children'].append(line.split()[2].replace('@',''))
    else:
      for j in range(i,len(lines)-1):
        line = lines[j]
        level = line[0]
        if 'FAM' in line.split() and level == '0':
          family['id'] = line.split()[1].replace('@','')
        if 'MARR' in line.split():
          family['are divorced'] = False
          family['married'] = lines[j+1].split('DATE')[1].replace('\n','')
        if 'DIV' in line.split():
          family['are divorced'] = True
          family['divorced'] = lines[j+1].split('DATE')[1].replace('\n','')
        if 'HUSB' in line.split():
          family['Husband ID'] = line.split()[2].replace('@','')
          family['Husband Name'] = individuals_id_and_name[family['Husband ID']]
        if 'WIFE' in line.split():
          family['Wife ID'] = line.split()[2].replace('@','')
          family['Wife Name'] = individuals_id_and_name[family['Wife ID']]
        if 'CHIL' in line.split():
          if 'children' in family: 
            family['children'].append(line.split()[2].replace('@',''))
          else:
            family['children'] = []
            family['children'].append(line.split()[2].replace('@',''))

    families.append(family)

  return pd.DataFrame(families)

def getIDIndices(filename):
  indices = {}
  f = open(filename, "r")
  lines = f.readlines()
  for i in range(0,len(lines)):
    line = lines[i]
    level = line[0]
    if 'INDI' in line.split() and level == '0':
      indices[line.split()[1].replace('@','')] = i
  return indices


def getFamilyIndices(filename):
  indices = {}
  f = open(filename, "r")
  lines = f.readlines()
  for i in range(0,len(lines)):
    line = lines[i]
    level = line[0]
    if 'FAM' in line.split() and level == '0':
      indices[line.split()[1].replace('@','')] = i
  return indices

def areIndividualDatesBeforeCurrentDate(individuals_dataframe, id_indices):
  #birthdays
  for id in individuals_dataframe['id']:
    birthday_date = individuals_dataframe.loc[individuals_dataframe['id'] == id, 'birthday'].iloc[0]
    if isDateBeforeCurrentDate(datetime.strptime(birthday_date," %d %b %Y")) == False:
      print("ERROR: INDIVIDUAL: US01: " + str(id_indices[id]) + ": " + id + " Birthday" + birthday_date + " occurs in the future")

  #deaths
  is_alive = individuals_dataframe.loc[individuals_dataframe['id'] == id, 'alive'].iloc[0]
  if is_alive == False:
    death_date = individuals_dataframe.loc[individuals_dataframe['id'] == id, 'death'].iloc[0]
    if isDateBeforeCurrentDate(datetime.strptime(death_date," %d %b %Y")) == False:
      print("ERROR: INDIVIDUAL: US01: " + str(id_indices[id]) + ": " + id + " Death" + death_date + " occurs in the future")

def areFamilyDatesBeforeCurrentDate(families_dataframe, family_id_indices):
  for id in families_dataframe['id']:
    marriage_date = families_dataframe.loc[families_dataframe['id'] == id, 'married'].iloc[0]
    if isDateBeforeCurrentDate(datetime.strptime(marriage_date," %d %b %Y")) == False:
      print("ERROR: FAMILY: US01:" + str(family_id_indices[id]) + ": " + id + " Married" + marriage_date + " occurs in the future")
    
  are_divorced = families_dataframe.loc[families_dataframe['id'] == id, 'are divorced'].iloc[0]
  if are_divorced:
    divorce_date = families_dataframe.loc[families_dataframe['id'] == id, 'divorced'].iloc[0]
    if isDateBeforeCurrentDate(datetime.strptime(divorce_date," %d %b %Y")) == False:
      print("ERROR: FAMILY: US01:" + str(family_id_indices[id]) + ": " + id + " Divorce" + divorce_date + " occurs in the future")