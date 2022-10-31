import os
import pandas as pd

def list_living_single(individuals, families):
    living_over30_people = [(row['id'], row['age']) for index,row in individuals.iterrows() if row['alive'] and row['age'] > 30]
    single_people = [(row['id'], row['age']) for index,row in individuals.iterrows() if str(row['spouse'])=='nan']

    living_single = [x for x in living_over30_people if x in single_people]

    print("US31: The list of living people that are single and over 30: " + str(living_single))
