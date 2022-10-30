import os
import pandas as pd

def list_living_single(individuals, families):
    individuals_list = set(sorted(list(individuals[['id']])))
    families_list = set(sorted(list(set(list(families[['Husband ID']]) + list(families[['Wife ID']])))))

    return_string = "The list of living people that are single: "
    return_string = ','.join(list(individuals_list - families_list))

    print(return_string)