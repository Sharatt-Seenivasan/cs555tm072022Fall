import pandas as pd
import parser
import math

def no_marriages_to_descendants(individuals,families,family_id_indices):
    for index, row in families.iterrows():
        wife_id = row['Wife ID']
        husband_id = row['Husband ID']
        if husband_id in getDescendants(wife_id,individuals,families):
            print("ERROR: FAMILY: US17: Line Index # " + str(family_id_indices[row['id']]) + ": " + " Wife " + wife_id + " in Family " + row['id'] + " is married to their descendant!")
        if wife_id in getDescendants(husband_id,individuals,families):
            print("ERROR: FAMILY: US17: Line Index # " + str(family_id_indices[row['id']]) + ": " + " Husband " + husband_id_id + " in Family " + row['id'] + " is married to their descendant!")

def getDescendants(person_id, individuals_dataframe, families_dataframe):
    descendants = []
    spouse_type = ''
    if individuals_dataframe.loc[individuals_dataframe['id'] == person_id, 'gender'].iloc[0] == 'M':
        spouse_type = 'Husband ID'
    else:
        spouse_type = 'Wife ID'
    for index, row in families_dataframe.iterrows():
        if row[spouse_type] == person_id:
            if str(row['children']) != 'nan':
                for child in row['children']:
                    descendants.append(child)
                    descendants.extend(getDescendants(child,individuals_dataframe,families_dataframe))
    return descendants
