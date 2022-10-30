import pandas as pd 

def getDeadPeople(individuals_dataframe):
    print("US29: List of dead people")
    deadPeople = [(row['id'], row['name']) for index, row in individuals_dataframe.iterrows() if not row['alive']]
    return deadPeople