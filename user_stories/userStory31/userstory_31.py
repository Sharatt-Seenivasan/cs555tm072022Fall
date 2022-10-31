import numpy as np
import pandas as pd

def list_living_single(individuals, families):
    individuals_list = list(individuals['id'])
    living_people = [row['id'] for index,row in individuals.iterrows() if row['alive']]
    single_people = [row['id'] for index,row in individuals.iterrows() if np.all(pd.isna(row['spouse']))]

    living_married = [x for x in living_people if x in single_people]

    print("US31: The list of living people that are married: " + str(living_married))