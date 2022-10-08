def no_sibline_marriage(individuals, families):
    for index, row in families.iterrows():
        husband_id = row['Husband ID']