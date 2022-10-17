import pandas as pd

def no_sibline_marriage(individuals, families):
    all_legal_marriages = True
    
    for index, row in families.iterrows():
        husband_child_family = individuals.loc[individuals['id'] == row['Husband ID'], 'child'].iloc[0]
        wife_child_family = individuals.loc[individuals['id'] == row['Wife ID'], 'child'].iloc[0]

        # check the parents of the spouses
        if not pd.isna(husband_child_family) and not pd.isna(wife_child_family):
            husband_father = families.loc[families['id'] == husband_child_family, 'Husband ID'].iloc[0]
            husband_mother = families.loc[families['id'] == husband_child_family, 'Wife ID'].iloc[0]
            wife_father = families.loc[families['id'] == wife_child_family, 'Husband ID'].iloc[0]
            wife_mother = families.loc[families['id'] == wife_child_family, 'Wife ID'].iloc[0]
        
            if husband_father == wife_father and husband_mother == wife_mother:
                print("ERROR: FAMILY: US18: " + row['id'] + " is a sibling marriage sharing the same parents!")
                all_legal_marriages = False
            elif husband_father == wife_father:
                print("ERROR: FAMILY: US18: " + row['id'] + " is a half-sibling marriage sharing the same father!")
                all_legal_marriages = False
            elif husband_mother == wife_mother:
                print("ERROR: FAMILY: US18: " + row['id'] + " is a half-sibling marriage sharing the same mother!")
                all_legal_marriages = False

    if all_legal_marriages:
        print("File has no sibling marriages.")