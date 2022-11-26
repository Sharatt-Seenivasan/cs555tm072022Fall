from datetime import date, datetime
import os
import pandas as pd

def is_within_last_30_days(event_date):
    #check if value is nan
    if pd.isna(event_date):
        return False
    return (date.today() - datetime.strptime(event_date," %d %b %Y").date()).days <= 30

# List all living spouses and descendants of people in a GEDCOM file who died in the last 30 days
def list_recent_survivors(individuals, families):
    recent_survivors = []
    for index, row in individuals.iterrows():
        if is_within_last_30_days(row['death']):
            dead_person = row['id']
            #check if descendents are alive
            living_spouses = []
            living_descendents = []
            for family in row['spouse']:
                family_row = families.loc[families['id'] == family]

                if family_row.at[family_row.index[0], 'Husband ID'] != dead_person:
                    spouse_id = family_row.at[family_row.index[0], 'Husband ID']
                else:
                    spouse_id = family_row.at[family_row.index[0], 'Wife ID']

                # WIll bad added unsorted
                children_list = family_row.at[family_row.index[0], 'children']
                
                for index_2, row_2 in individuals.iterrows():
                    if (row_2['id'] == spouse_id and row_2['alive']):
                        living_spouses.append((row_2['id'], row_2['age']))
                    if (row_2['id'] in children_list and row_2['alive']):
                        living_descendents.append((row_2['id'], row_2['age']))

            new_recent_survivors = {
                'name': (row['id'], row['age']),
                'living spouses': living_spouses, 
                'living descendents': living_descendents
            }
            recent_survivors.append(new_recent_survivors)

    print("US31: The list of all living spouses and descendents of people who died in the last 30 days: " + str(recent_survivors))
