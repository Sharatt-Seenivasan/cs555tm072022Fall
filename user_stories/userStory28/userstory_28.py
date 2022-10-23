import pandas as pd

def sortChildrenByAge(children, individual_dataframe):
    child_ages = []
    for child in children:
        age = individual_dataframe.loc[individual_dataframe['id'] == child][0]
        child_ages.append((child,age))
    child_ages.sort(key = lambda x : x[1])
    sorted_children = [child in (child,ages) in child_ages]
    return sorted_children