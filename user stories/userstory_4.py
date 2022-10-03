import pandas as pd
import parser
import math

def marriage_before_divorce(gedcom_file):
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
    error_type = "US04 Marriage before divorce"
    xls = pd.ExcelFile('out.xlsx')
    df2=pd.read_excel(xls,'Families')
    for row in df2.itertuples(index=False):
        if not type(row.married)==float and not type(row.divorced)==float:
            marr = row.married
            divv = row.divorced
            if marr > divv:
                message = "Divorced date "+str(divv)+", Before Marriage date "+str(marr)+ " , therefore it is not valid."
                #save_invalidfor_print(res["FAMID"], "US04", message)
                #print(message)  
                return False
            
    return True  
                

    
