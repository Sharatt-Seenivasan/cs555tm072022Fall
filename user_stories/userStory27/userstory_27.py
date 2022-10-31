import pandas as pd
import parser
import math
    
def individual_ages(individuals_dataframe,id_indices):
    for index,row in individuals_dataframe.iterrows():
        name=row['name']
        age=row["age"]
        if age < 0 or math.isnan(age):
            message="ERROR: INDIVIDUAL: US27: " + str(id_indices[row['id']]) + ": " + row['id'] + " Name: " + name + " does not have a valid age."
            print(message)
        else:
            print("NAME:"+ name +",Age:" + str(age))

            
(individuals,individuals_id_and_name) = createIndDataframe("test_data.ged")
individual_ages(individuals,getIDIndices("test_data.ged"))

