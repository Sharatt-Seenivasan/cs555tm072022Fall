from collections import Counter
import os
import pandas as pd

# Sort the list of IDs and check for duplicates
def check_id(id_list):
    c1 = Counter(id_list)
    c2 = Counter(set(id_list))
    diff = c1-c2
    diff_list = sorted(set(diff.elements()))
    
    return_string = ""
    for x in diff_list:
        return_string += ("ID " + x + " is not a unique ID.\n")
    if return_string != "":
        print(return_string[:-1])

    return len(diff_list) == 0

def unique_ids(individuals, families):
    individual_id_list = sorted(list(individuals['id']))
    family_id_list = sorted(list(families['id']))

    has_unique_individuals = check_id(individual_id_list)
    has_unique_families = check_id(family_id_list)
    all_unique = has_unique_individuals and has_unique_families

    if all_unique:
        print("File has all unique IDs.")
    
    return all_unique


#filename = os.path.abspath(os.path.dirname(__file__)) + '/../test_data.xlsx'
#filename = os.path.abspath(os.path.dirname(__file__)) + '/../testcases/userstory_7/uniqueIDsTestData1.xlsx'
#unique_ids(filename)