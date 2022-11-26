from datetime import date, datetime
import os
import pandas as pd

def is_within_next_30_days(event_date):
    if event_date == 'nan':
        return False
    return (datetime.strptime(event_date," %d %b %Y").date().replace(year=today.year) - date.today()).days() <= 30

# List all living couples in a GEDCOM file whose marriage anniversaries occur in the next 30 days
# Assuming they still have to still be married
def list_upcoming_anniversaries(individuals, families):
    upcoming_anniversaries = []
    for index, row in families.iterrows():
        if is_within_next_30_days(row['married']) and not row['are divorced']:
            is_husband_alive = False
            is_wife_alive = False
            husband_id = row['Husband ID']
            wife_id = row['Wife ID']
            for index, row_2 in individuals.iterrows():
                if (row_2['id'] == husband_id and row_2['alive']):
                    is_husband_alive = True
                if (row_2['id'] == wife_id and row_2['alive']):
                    is_wife_alive = True
            if (is_husband_alive and is_wife_alive):
                upcoming_anniversaries.append((husband_id, wife_id))

    print("US31: The list of all living couples with marriage anniversaries in the next 30 days: " + str(upcoming_anniversaries))
