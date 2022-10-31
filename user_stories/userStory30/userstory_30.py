import os
import pandas as pd

def list_living_married(individuals, families):
    individuals_list = sorted(list(individuals[['id']]))
    families_list = sorted(list(set(list(families[['Husband ID']]) + list(families[['Wife ID']]))))

    return_string = "The list of living people that are married: "
    return_string = ','.join(families_list)

    print(return_string)