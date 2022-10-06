import pandas as pd
import parser
import math

def birth_before_death(individuals_dataframe, id_indices):
    df = individuals_dataframe
    for row in df.itertuples(index=False):
        if not type(row.death) == float or not math.isnan(row.death):
            if compareDates(row.birthday, row.death):
                print("ERROR: INDIVIDUAL: US03: " + row.id + ": " + "Died " + row.death + " before born " + row.birthday)