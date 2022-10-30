import pandas as pd
import parser
import math

def no_marriages_to_descendants(families):
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
                            message="ERROR:USERSTORY17 Parents should not marry any of their descendants"
                            print(message)
                            return message
                        

