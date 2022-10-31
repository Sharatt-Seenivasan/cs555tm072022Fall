import pandas as pd

def isChildInFamily(person_id, families):
    for index, row in families.iterrows():
        if str(row['children']) != 'nan' and person_id in row['children']:
            return True
    return False

def no_cousins_marriage(individuals, families):
    for index, row in families.iterrows():
        wife_id = row['Wife ID']
        husband_id = row['Husband ID']
        if husband_id in getFirstCousins(wife_id,individuals,families):
            print("ERROR: FAMILY: US19: Line Index # " + str(row['index']) + ": Family " + row['id'] + " is a marriage between first cousins!")
        # if wife_id in getFirstCousins(husband_id,individuals,families):
            # print("ERROR: FAMILY: US20: Line Index # " + str(row['index']) + ": Family " + row['id'] + " is a marriage between first cousins!")

    # for i, row in families.iterrows():
        # if row['Husband ID'] in individuals['id'].values and row['Wife ID'] in individuals['id'].values:
            # if isChildInFamily(row['Husband ID'], families) and isChildInFamily(row['Wife ID'], families):
                # husband_family = individuals.loc[individuals['id'] == row['Husband ID'], 'child'].iloc[0]
                # wife_family = individuals.loc[individuals['id'] == row['Wife ID'], 'child'].iloc[0]

                # #Check grandparents of the husband and wife
                # if not pd.isna(husband_family) and not pd.isna(wife_family):
                    # husband_father = families.loc[families['id'] == husband_family, 'Husband ID'].iloc[0]
                    # husband_mother = families.loc[families['id'] == husband_family, 'Wife ID'].iloc[0]
                    # wife_father = families.loc[families['id'] == wife_family, 'Husband ID'].iloc[0]
                    # wife_mother = families.loc[families['id'] == wife_family, 'Wife ID'].iloc[0]

                    # #Define grandparents of the husband
                    # if isChildInFamily(husband_father, families) and isChildInFamily(husband_mother, families) and isChildInFamily(wife_father, families) and isChildInFamily(wife_mother, families):
                        # husband_father_father = families.loc[families['id'] == husband_father, 'Husband ID'].iloc[0]
                        # husband_father_mother = families.loc[families['id'] == husband_father, 'Wife ID'].iloc[0]
                        # husband_mother_father = families.loc[families['id'] == husband_mother, 'Husband ID'].iloc[0]
                        # husband_mother_mother = families.loc[families['id'] == husband_mother, 'Wife ID'].iloc[0]

                        # #Define grandparents of the wife
                        # wife_father_father = families.loc[families['id'] == wife_father, 'Husband ID'].iloc[0]
                        # wife_father_mother = families.loc[families['id'] == wife_father, 'Wife ID'].iloc[0]
                        # wife_mother_father = families.loc[families['id'] == wife_mother, 'Husband ID'].iloc[0]
                        # wife_mother_mother = families.loc[families['id'] == wife_mother, 'Wife ID'].iloc[0]

                        # #Perform checks on sharing grandparents
                        # if husband_father_father == wife_father_father or husband_father_father == wife_mother_father:
                            # print('ERROR: FAMILY: US19: ' + row['id'] + ' is a first cousin marriage sharing the same grandfather!')
                            # legal_marriages = False
                        # elif husband_father_mother == wife_father_mother or husband_father_mother == wife_mother_mother:
                            # print('ERROR: FAMILY: US19: ' + row['id'] + ' is a first cousin marriage sharing the same grandmother!')
                            # legal_marriages = False
                        # elif husband_mother_father == wife_father_father or husband_mother_father == wife_mother_father:
                            # print('ERROR: FAMilY: US19: ' + row['id'] + ' is a first cousin marriage sharing the same grandfather!')
                            # legal_marriages = False
                        # elif husband_mother_mother == wife_father_mother or husband_mother_mother == wife_mother_mother:
                            # print('ERROR: FAMILY: US19: ' + row['id'] + ' is a first cousin marriahe sharing the same grandmother!')
                            # legal_marriages = False
                

def getFirstCousins(person_id, individuals_dataframe, families_dataframe):
    cousins = []
    for index, row in families_dataframe.iterrows():
        husband_id = row['Husband ID']
        wife_id = row['Wife ID']
        if str(row['children']) != 'nan':
            if person_id in row['children']:
                cousins.extend(getNiblings(husband_id,individuals_dataframe, families_dataframe))
                cousins.extend(getNiblings(wife_id,individuals_dataframe, families_dataframe))
    return cousins


def getNiblings(person_id, individuals_dataframe, families_dataframe):
    niblings = []
    spouse_type = ''
    for index, row in families_dataframe.iterrows():
        if str(row['children']) != 'nan':
            if person_id in row['children']:
                for child in row['children']:
                    if child != person_id:
                        niblings.extend(getChildren(child,individuals_dataframe, families_dataframe))
    return niblings

def getChildren(person_id, individuals_dataframe, families_dataframe):
    children = []
    spouse_type = ''
    if individuals_dataframe.loc[individuals_dataframe['id'] == person_id, 'gender'].iloc[0] == 'M':
        spouse_type = 'Husband ID'
    else:
        spouse_type = 'Wife ID'
    for index, row in families_dataframe.iterrows():
        if row[spouse_type] == person_id:
            if str(row['children']) != 'nan':
                for child in row['children']:
                    children.append(child)
    return children
