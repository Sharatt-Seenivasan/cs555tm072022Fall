import pandas as pd
from isDateBeforeCurrentDate import *

filename = "test_data.ged"

def unique_families(filename):
    (individuals,individuals_id_and_name) = createIndDataframe(filename)
    families = createFamilyDataframe(filename, individuals_id_and_name)
    #temp = families.head(1)
    #families = pd.concat([families, temp], ignore_index = True)
    #families.iat[5,0] = 'F6'
    family_ids = families[['Husband ID', 'Wife ID']]
    check_duplicated = list(family_ids.duplicated())

    for i in range(len(check_duplicated)):
        if (check_duplicated[i]):
            print("Family ID", families.loc[i].at['id'], "is not a unique ID with a unique spouse")

unique_families(filename)