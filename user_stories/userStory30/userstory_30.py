import pandas as pd

def list_living_married(individuals, families):
    individuals_list = list(individuals['id'])
    living_people = [row['id'] for index,row in individuals.iterrows() if row['alive']]
    married_people = [row['id'] for index,row in individuals.iterrows() if row['spouse']]
    living_married = [x for x in living_people if x in married_people]

    print("US30: The list of living people that are married: " + str(living_married))
