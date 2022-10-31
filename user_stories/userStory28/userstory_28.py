import pandas as pd

def listChildrenByAge(individual_dataframe,families_dataframe):
    print("US28: Children in each family ordered by age.")
    for index, row in families_dataframe.iterrows():
        print("Children in Family " + row['id'] + ":") 
        child_ages = []
        if str(row['children']) != 'nan':
            for child in row['children']:
                age = individual_dataframe.loc[individual_dataframe['id'] == child, 'age'].iloc[0]
                child_ages.append((child,age))
        child_ages.sort(key = lambda x : x[1], reverse=True)
        sorted_children = [child for (child,age) in child_ages]
        print(sorted_children)
