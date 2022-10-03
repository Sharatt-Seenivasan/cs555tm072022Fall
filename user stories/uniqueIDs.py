from collections import Counter
import os
import pandas as pd

# Sort the list of IDs and check for duplicates
def check_id(id_list):
    c1 = Counter(id_list)
    c2 = Counter(set(id_list))
    diff = c1-c2
    diff_list = set(diff.elements())
    for x in diff_list:
        print("ID", x, "is not a unique ID.")
    return len(diff_list) == 0

def unique_ids(filename):
    #(individuals,individuals_id_and_name) = createIndDataframe(filename)
    #families = createFamilyDataframe(filename, individuals_id_and_name)
    individuals = pd.read_excel(io=filename, sheet_name='Individuals')
    individual_id_list = sorted(list(individuals['id']))
    families = pd.read_excel(io=filename, sheet_name='Families')
    family_id_list = sorted(list(families['id']))

    has_unique_individuals = check_id(individual_id_list)
    has_unique_families = check_id(family_id_list)

    if (has_unique_individuals and has_unique_families):
        print("File has all unique IDs.")

#filename = os.path.abspath(os.path.dirname(__file__)) + '/../test_data.xlsx'
#unique_ids(filename)