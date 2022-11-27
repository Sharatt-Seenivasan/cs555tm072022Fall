import pandas as pd

# List all living married people in a GEDCOM file
# Bug: Does not check if person is divorced
def list_living_married(individuals, families):
    living_people = [(row['id'], row['age']) for index,row in individuals.iterrows() if row['alive']]
    married_people = [(row['id'], row['age']) for index,row in individuals.iterrows() if type(row['spouse']) is list]
    living_married = [x for x in living_people if x in married_people]

    print("US30: The list of living people that are married: " + str(living_married))
