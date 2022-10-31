import pandas as pd

def no_newphew_niece_marriage(individuals, families):
    for i, row in families.iterrows():
        if row['Husband ID'] in individuals['id'].values and row['Wife ID'] in individuals['id'].values:
            husband_family = individuals.loc[individuals['id'] == row['Husband ID'], 'child'].iloc[0]
            wife_family = individuals.loc[individuals['id'] == row['Wife ID'], 'child'].iloc[0]


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

                if husband_father_father == wife_father and husband_father_mother == wife_mother:
                    print('ERROR: FAMILY: US20: ' + row['id'] + ' is a marriage between a nephew and an aunt!')
                elif husband_mother_father == wife_father and husband_mother_mother == wife_mother:
                    print('ERROR: FAMILY: US20: ' + row['id'] + ' is a marriage between a nephew and an aunt!')
                elif wife_father_father == husband_father and wife_father_mother == husband_mother:
                    print('ERROR: FAMILY: US20: ' + row['id'] + ' is a marriage between a niece and an uncle!')
                elif wife_mother_father == husband_father and wife_mother_mother == husband_mother:
                    print('ERROR: FAMILY: US20: ' + row['id'] + ' is a marriage between a niece and an uncle!')

