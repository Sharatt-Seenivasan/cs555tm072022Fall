import pandas as pd
import parser
import math
    
def parents_not_too_old(individuals,families):
    for index, row in families.iterrows():
        if not type(row.children)==float or not math.isnan(row.children):
            age_of_mother=individuals.loc[individuals['id']==row['Wife ID'],'age'].iloc[0]
            age_of_father=individuals.loc[individuals['id']==row['Husband ID'],'age'].iloc[0]
            for child in row.children:
                age_of_child=individuals.loc[individuals['id']==child,'age'].iloc[0]
                if (age_of_mother-age_of_child)>=20 or (age_of_father-age_of_child)>=80:
                        message= "ERROR:USERSTORY12 parents are too old"
                        print(message)     
    return message

