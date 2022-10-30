import pandas as pd
import parser
import math
def parents_not_too_old(individuals_dateframe,families_dataframe):
    for i in range(len(families_dataframe)):
        if "children" in families_dataframe[i]:
            age_of_mother=get_age(families_dataframe[i]["Wife ID"],individuals_dateframe)
            age_of_father=get_age(families_dataframe[i]["Husband ID"],individuals_dateframe)
            ages_of_children=get_children_age(families_dataframe[i]["children"],individuals_dateframe)                       
            for child_age in ages_of_children:
                if (age_of_mother-child_age)>=60 or (age_of_father-child_age)>=80:
                    message= "ERROR:USERSTORY12 parents are too old"
                    print(message)
    return message                                    
def get_age(personid,individuals_dateframe):
    for i in range(len(individuals_dateframe)):
        if individuals_dateframe[i]["id"] ==personid:
            return individuals_dateframe[i]["age"]       
def get_children_age(children,individuals_dateframe):
    array_of_children_ages=[]
    for child in children:
        for i in range(len(individuals_dateframe)):
            if individuals_dateframe[i]["id"] ==child:
                array_of_children_ages.append(individuals_dateframe[i]["age"])        
    return array_of_children_ages

