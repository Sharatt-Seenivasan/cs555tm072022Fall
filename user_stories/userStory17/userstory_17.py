import pandas as pd
import parser
import math

def no_marriages_to_descendants(families,family_id_indices):
    message="there are no such marriages"
    for index, row in families.iterrows():
        if not type(row.children)==float or not math.isnan(row.children):
            ids_of_children=row.children
            for child in row.children:
                for index,row1 in families.iterrows():
                    wifeid= row1['Wife ID']
                    husbandid=row1['Husband ID']
                    if child ==wifeid or child==husbandid:
                        ids_of_desc=row1.children
                        if row['Wife ID']==ids_of_desc[0] or row['Husband ID']==ids_of_desc[0]:
                            message="ERROR: FAMILY: US17: " + str(family_id_indices[row['id']]) + ": " + row['id'] + " Id of child: " + str(ids_of_desc[0]) + " ,Wife ID: " + str(row['Wife ID'])+ " ,Husband ID: "+ str(row['Husband ID'])
                            print(message)
    return message

(individuals,individuals_id_and_name) = createIndDataframe("test_data.ged")
families = createFamilyDataframe("test_data.ged", individuals_id_and_name)
no_marriages_to_descendants(families,getFamilyIndices("test_data.ged"))

