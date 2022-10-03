import pandas as pd
import parser
import math

def birth_before_death(gedcom_file):
    filename = 'test_data.ged'
    writer = pd.ExcelWriter('out.xlsx')
    (individuals,individuals_id_and_name) = parser.save_ind_data(filename)
    families = parser.save_family_data(filename, individuals_id_and_name)
    pd.DataFrame(individuals).to_excel(writer, sheet_name="Individuals")
    pd.DataFrame(families).sort_values(by = ['id']).to_excel(writer, sheet_name="Families")
    writer.save()
    df=pd.read_excel('out.xlsx')
    xls = pd.ExcelFile('out.xlsx')
    df1=pd.read_excel(xls,'Individuals')
    df2=pd.read_excel(xls,'Families')
    return_flag=True
    xls = pd.ExcelFile('out.xlsx')
    df=pd.read_excel(xls,'Individuals')
    for row in df.itertuples(index=False):
        if not type(row.death)==float or not math.isnan(row.death):
            if row.birthday>row.death:
                return_flag=False
                
    return return_flag


                
    
