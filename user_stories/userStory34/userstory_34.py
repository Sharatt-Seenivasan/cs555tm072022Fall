import pandas
from datetime import *
from dateutil.relativedelta import *

def large_age_difference(individuals, families):
    largelist = []
    for index, row in families.iterrows():
        if row['married'] == row['married']:
            marriage_time = datetime.strptime(row['married'], " %d %b %Y")

            if row['Husband ID'] in individuals['id'].values:
                husband_birth = individuals.loc[individuals['id'] == row['Husband ID'], 'birthday'].iloc[0]
                husband_birth_time = datetime.strptime(husband_birth, " %d %b %Y")
                husband_marriage_age = relativedelta(marriage_time, husband_birth_time).years

                if row['Wife ID'] in individuals['id'].values:
                    wife_birth = individuals.loc[individuals['id'] == row['Wife ID'], 'birthday'].iloc[0]
                    wife_birth_time = datetime.strptime(wife_birth, " %d %b %Y")
                    wife_marriage_age = relativedelta(marriage_time, wife_birth_time).years

                    if husband_marriage_age >= (2 * wife_marriage_age) or wife_marriage_age >= (2 * husband_marriage_age):
                        largelist.append("US:34 List of large age differences: Husband age " + str(husband_marriage_age) + " Wife age " + str(wife_marriage_age))

    return largelist

