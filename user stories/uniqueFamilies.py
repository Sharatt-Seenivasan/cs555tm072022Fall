import os
import pandas as pd

def unique_families(filename):
    families = pd.read_excel(io=filename, sheet_name='Families')
    #temp = families.head(1)
    #families = pd.concat([families, temp], ignore_index = True)
    #families.iat[5,0] = 'F6'
    family_ids = families[['Husband ID', 'Wife ID']]
    check_duplicated = list(family_ids.duplicated())

    for i in range(len(check_duplicated)):
        if (check_duplicated[i]):
            print("Family ID", families.loc[i].at['id'], "is not a unique ID with a unique spouse.")
    
    if (not any(check_duplicated)):
        print("File has all unique families.")

#filename = os.path.abspath(os.path.dirname(__file__)) + '/../test_data.xlsx'
#unique_families(filename)