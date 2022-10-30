import pandas as pd
import parser
import math
import gedcom_master

def no_marriages_to_descendants(families_dataframe):
    for i in range(len(families_dataframe)):
        if "children" in families_dataframe[i]:
            ids_of_children=families_dataframe[i]["children"]
            for j in range(len(ids_of_children)):
                for k in range(len(families_dataframe)):
                    if ids_of_children[j]== families_dataframe[k]["Wife ID"] or ids_of_children[j]== families_dataframe[k]["Husband ID"]:
                        ids_of_desc=families_dataframe[k]["children"]
                        if families_dataframe[i]["Wife ID"] == ids_of_desc[0] or families_dataframe[i]["Husband ID"]== ids_of_desc[0]:
                            print("ERROR:USERSTORY17 Parents should not marry any of their descendants")
                            message="ERROR:USERSTORY17 Parents should not marry any of their descendants"
                            return message
                        

