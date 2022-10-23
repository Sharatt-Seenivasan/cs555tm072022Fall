import pandas
from datetime import *
from dateutil.relativedelta import *

def marriage_after_14(individuals, families):
    legal_marriage_age = 14
    all_legal_marriages = True

    for index, row in families.iterrows():
        if row['married'] == row['married']:
            marriage_time = datetime.strptime(row['married'], " %d %b %Y")

            #error check if husband in individuals does not exist
            if row['Husband ID'] in individuals['id'].values: 
                husband_birth = individuals.loc[individuals['id'] == row['Husband ID'], 'birthday'].iloc[0]
                husband_birth_time = datetime.strptime(husband_birth, " %d %b %Y")
                husband_marriage_age = relativedelta(marriage_time, husband_birth_time).years

                if row['Wife ID'] in individuals['id'].values: 
                    wife_birth = individuals.loc[individuals['id'] == row['Wife ID'], 'birthday'].iloc[0]
                    wife_birth_time = datetime.strptime(wife_birth, " %d %b %Y")
                    wife_marriage_age = relativedelta(marriage_time, wife_birth_time).years

                if husband_marriage_age < legal_marriage_age and wife_marriage_age < legal_marriage_age:
                    print("ERROR: FAMILY: US10: Both spouses from family " + row['id'] + " married before the age of 14!")
                    all_legal_marriages = True
                elif husband_marriage_age < legal_marriage_age:
                    print("ERROR: FAMILY: US10: Husband from family " + row['id'] + " married before the age of 14!")
                    all_legal_marriages = True
                elif wife_marriage_age < legal_marriage_age:
                    print("ERROR: FAMILY: US10: Wife from family " + row['id'] + " married before the age of 14!")
                    all_legal_marriages = True

    #if all_legal_marriages:
        #print("File has all marriages after 14.")

    return all_legal_marriages
