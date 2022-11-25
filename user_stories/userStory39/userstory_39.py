from datetime import date, datetime
import os
import pandas as pd

def is_within_last_30_days(event_date):
    #check if value is nan
    if event_date == 'nan':
        return False
    return abs(date.today() - datetime.strptime(event_date," %d %b %Y")).days() <= 30

# List all living couples in a GEDCOM file whose marriage anniversaries occur in the next 30 days
def list_upcoming_anniversaries(individuals, families):
    upcoming_anniversaries = []
    for index, row in individuals.iterrows():
        if is_within_last_30_days(row['death']):
            dead_person = row['id']
            #check if descendents are alive
            living_spouses = []
            living_descendents = []
            for family in row['spouse']:
                family_row = families[families['id'] == family]
                #family_row = families.loc[families['id'] == family]

                spouse_id = family_row['Husband ID'] if family_row['Husband ID'] != dead_person else family_row['Wife ID']
                children_list = family_row['children']
                
                for index, row_2 in individuals.iterrows():
                    if (row_2['id'] == spouse_id and row_2['alive']):
                        living_spouses.append((row_2['id'], row_2['age']))
                    if (row_2['id'] in children_list and row_2['alive']):
                        living_descendents.append((row_2['id'], row_2['age']))

            new_recent_survivors = {
                'name': row['id'], 
                'age': row['age'], 
                'living spouses': living_spouses, 
                'living descendents': living_descendents
            }
            recent_survivors.append(new_recent_survivors)

    print("US31: The list of all living spouses and descendents of people who died int he last 30 days: " + str(recent_survivors))
