import os
import pandas as pd

def list_living_single(individuals, families):
    individuals_list = list(individuals['id'])
    living_over30_people = [row['id'] for index,row in individuals.iterrows() if row['alive'] and row['age'] > 30]
    single_people = [row['id'] for index,row in individuals.iterrows() if str(row['spouse'])=='nan']

    living_single = [x for x in living_over30_people if x in single_people]

    print("US31: The list of living people that are single: " + str(living_single)
