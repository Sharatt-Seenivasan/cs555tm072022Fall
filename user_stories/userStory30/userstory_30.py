import os
import pandas as pd

def list_living_married(individuals, families):
    individuals_list = list(individuals['id'])
    families_list = list(families['Husband ID']) + list(families['Wife ID'])

    return_string = "The list of living people that are married: "
    return_string += ','.join(families_list)

    print(individuals_list)