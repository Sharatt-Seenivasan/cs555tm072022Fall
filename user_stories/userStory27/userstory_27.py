import pandas as pd
import parser
import math
    
def individual_ages(individuals_dataframe):
    for index,row in individuals_dataframe.iterrows():
        name=row['name']
        age=row["age"]
        if age < 0 or math.isnan(age):
            message= "ERROR: INDIVIDUAL: US27: " + name + " does not have a valid age."
            print(message)

