import os
import pandas as pd

def unique_families(families):
    #families = pd.read_excel(io=filename, sheet_name='Families')
    #temp = families.head(1)
    #families = pd.concat([families, temp], ignore_index = True)
    #families.iat[5,0] = 'F6'
    family_ids = families[['Husband ID', 'Wife ID']]
    check_duplicated = list(family_ids.duplicated())

    return_string = ""
    for i in range(len(check_duplicated)):
        if (check_duplicated[i]):
            return_string += ("Family ID " + families.loc[i].at['id'] + " is not a unique ID with a unique spouse.")
    if return_string != "":
        print(return_string[:-1])
    
    all_unique = not any(check_duplicated)
    if all_unique:
        print("File has all unique families.")

    return all_unique


#filename = os.path.abspath(os.path.dirname(__file__)) + '/../test_data.xlsx'
#filename = os.path.abspath(os.path.dirname(__file__)) + '/../testcases/usetstory_8/uniqueFamiliesTestData1.xlsx'
#unique_families(filename)