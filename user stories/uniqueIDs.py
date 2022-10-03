from isDateBeforeCurrentDate import *
from collections import Counter

filename = "test_data.ged"

# Sort the list of IDs and check for duplicates
def check_id(id_list):
    c1 = Counter(id_list)
    c2 = Counter(set(id_list))
    diff = c1-c2
    diff_list = set(diff.elements())
    for x in diff_list:
        print("ID", x, "is not a unique ID")

def unique_ids(filename):
    (individuals,individuals_id_and_name) = createIndDataframe(filename)
    individual_id_list = sorted(list(individuals['id']))
    families = createFamilyDataframe(filename, individuals_id_and_name)
    #family_id_list = ['F1', 'F2', 'F3', 'F3', 'F4', 'F5']
    family_id_list = sorted(list(families['id']))
    check_id(family_id_list)
    check_id(individual_id_list)

unique_ids(filename)