import pandas as pd
import parser
import math

def marriage_before_divorce(families_dataframe):
    error_type = "US04 Marriage before divorce"
    df2 = families_dataframe
    for row in df2.itertuples(index=False):
        if not type(row.married) == float and not type(row.divorced) == float:
            marr = row.married
            divv = row.divorced
            if marr > divv:
                message = "ERROR: FAMILY: US03: " + row.id + ": Divorced date " + str(divv) + ", Before Marriage date " + str(marr) + " , therefore it is not valid."
                print(message)