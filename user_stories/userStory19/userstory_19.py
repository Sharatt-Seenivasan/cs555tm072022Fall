import pandas as pd

def no_cousins_marriage(individuals, families):
    legal_marriages = True

    for i, row in families.iterrows():
        if row['Husband ID'] in individuals['id'].values and row['Wife ID'] in individuals['id'].values:
            husband_family = individuals.loc[individuals['id'] == row['Husband ID'], 'child'].iloc[0]
            wife_family = individuals.loc[individuals['id'] == row['Wife ID'], 'child'].iloc[0]

            #Check grandparents of the husband and wife
            if not pd.isna(husband_family) and not pd.isna(wife_family):
                husband_father = families.loc[families['id'] == husband_family, 'Husband ID'].iloc[0]
                husband_mother = families.loc[families['id'] == husband_family, 'Wife ID'].iloc[0]
                wife_father = families.loc[families['id'] == wife_family, 'Husband ID'].iloc[0]
                wife_mother = families.loc[families['id'] == wife_family, 'Wife ID'].iloc[0]

                #Define grandparents of the husband
                husband_father_father = families.loc[families['id'] == husband_father, 'Husband ID'].iloc[0]
                husband_father_mother = families.loc[families['id'] == husband_father, 'Wife ID'].iloc[0]
                husband_mother_father = families.loc[families['id'] == husband_mother, 'Husband ID'].iloc[0]
                husband_mother_mother = families.loc[families['id'] == husband_mother, 'Wife ID'].iloc[0]

                #Define grandparents of the wife
                wife_father_father = families.loc[families['id'] == wife_father, 'Husband ID'].iloc[0]
                wife_father_mother = families.loc[families['id'] == wife_father, 'Wife ID'].iloc[0]
                wife_mother_father = families.loc[families['id'] == wife_mother, 'Husband ID'].iloc[0]
                wife_mother_mother = families.loc[families['id'] == wife_mother, 'Wife ID'].iloc[0]

                #Perform checks on sharing grandparents
                if husband_father_father == wife_father_father or husband_father_father == wife_mother_father:
                    print('ERROR: FAMILY: US19: ' + row['id'] + ' is a first cousin marriage sharing the same grandfather!')
                    legal_marriages = False
                elif husband_father_mother == wife_father_mother or husband_father_mother == wife_mother_mother:
                    print('ERROR: FAMILY: US19: ' + row['id'] + ' is a first cousin marriage sharing the same grandmother!')
                    legal_marriages = False
                elif husband_mother_father == wife_father_father or husband_mother_father == wife_mother_father:
                    print('ERROR: FAMilY: US19: ' + row['id'] + ' is a first cousin marriage sharing the same grandfather!')
                    legal_marriages = False
                elif husband_mother_mother == wife_father_mother or husband_mother_mother == wife_mother_mother:
                    print('ERROR: FAMILY: US19: ' + row['id'] + ' is a first cousin marriahe sharing the same grandmother!')
                    legal_marriages = False
                

