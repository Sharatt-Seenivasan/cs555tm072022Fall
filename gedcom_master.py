import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date
from user_stories import userstory_7, userstory_8, userstory_15

individuals = []
individuals_id_and_name = []
families = []
filename = 'test_data.ged'

allowed_tags = {
    0 : ['INDI','FAM','HEAD','TRLR','NOTE'],
    1 : ['NAME','SEX','BIRT','DEAT','FAMC','FAMS','MARR','HUSB','WIFE','CHIL','DIV'],
    2 : ['DATE']
}


def parse_gedcom(filename):
    f = open(filename, "r")
    for line in f:
        level = line[0]
        tag = ''
        arguments = ''
        if 'INDI' in line.split():
            tag = 'INDI'
            arguments = line.split()[1] + '\n'
        elif 'FAM' in line.split():
            tag = 'FAM'
            arguments = line.split()[1] + '\n'
        else:
            tag = line.split()[1]
        if (line.split(tag,1)[1])[1:] != '':
            arguments = (line.split(tag,1)[1])[1:]
        else:
            arguments = '\n'
            valid = 'N'
        if tag in allowed_tags[int(level)]:
            valid = 'Y'
        
        print('--> ' + line)
        print('<-- ' + level + '|' + tag + 
            '|' + valid + '|' + arguments)
  

def save_ind_data(filename):
    individuals = []
    individuals_id_and_name = {}
    f = open(filename, "r")
    lines = f.readlines()

    indices = []
    for i in range(0,len(lines)):
        line = lines[i]
        level = line[0]
        if 'INDI' in line.split() and level == '0':
            indices.append(i)

    for i in indices:
        is_dead = False
        person = {}
        if indices.index(i) != len(indices)-1:
            for j in range(i,indices[indices.index(i)+1]):
                line = lines[j]
                level = line[0]
                if 'INDI' in line.split() and level == '0':
                    person['id'] = line.split()[1].replace('@','')
                if 'NAME' in line.split():
                    person['name'] = line.split('NAME')[1].replace('\n','')
                    individuals_id_and_name[person['id']] = person['name']
                if 'SEX' in line.split() and level == '1':
                    person['gender'] = line.split()[2]
                if 'BIRT' in line.split():
                    person['birthday'] =  lines[j+1].split('DATE')[1].replace('\n','')
                if 'DEAT' in line.split():
                    is_dead = True
                    person['death'] = lines[j+1].split('DATE')[1].replace('\n','')
                if 'FAMC' in line.split():
                    person['child'] = line.split()[2].replace('@','')
                if 'FAMS' in line.split():
                    person['spouse'] = line.split()[2].replace('@','')
        else:
            for j in range(i,len(lines)-1):
                line = lines[j]
                level = line[0]
                if 'INDI' in line.split() and level == '0':
                    person['id'] = line.split()[1].replace('@','')
                if 'NAME' in line.split():
                    person['name'] = line.split('NAME')[1].replace('\n','')
                    individuals_id_and_name[person['id']] = person['name']
                if 'SEX' in line.split() and level == '1':
                    person['gender'] = line.split()[2]
                if 'BIRT' in line.split():
                    person['birthday'] = lines[j+1].split('DATE')[1].replace('\n','')
                if 'DEAT' in line.split():
                    is_dead = True
                    person['death'] = lines[j+1].split('DATE')[1].replace('\n','')
                if 'FAMC' in line.split():
                    person['child'] = line.split()[2].replace('@','')
                if 'FAMS' in line.split():
                    person['spouse'] = line.split()[2].replace('@','')

        if is_dead:
            person['age'] = relativedelta(pd.to_datetime(person['death'],infer_datetime_format=True), pd.to_datetime(person['birthday'],infer_datetime_format=True)).years
        else:
            today = date.today()
            person['age'] = relativedelta(today, pd.to_datetime(person['birthday'],infer_datetime_format=True)).years

        individuals.append(person)
        
    return (individuals,individuals_id_and_name)


def save_family_data(filename, individuals_id_and_name):
    families = []
    f = open(filename, "r")
    lines = f.readlines()

    indices = []
    for i in range(0,len(lines)):
        line = lines[i]
        level = line[0]
        if 'FAM' in line.split() and level == '0':
            indices.append(i)
    
    for i in indices:
        family = {}
        if indices.index(i) != len(indices)-1:
            for j in range(i,indices[indices.index(i)+1]):
                line = lines[j]
                level = line[0]
                if 'FAM' in line.split() and level == '0':
                    family['id'] = line.split()[1].replace('@','')
                if 'MARR' in line.split():
                    family['married'] = lines[j+1].split('DATE')[1].replace('\n','')
                if 'DIV' in line.split():
                    family['divorced'] = lines[j+1].split('DATE')[1].replace('\n','')
                if 'HUSB' in line.split():
                    family['Husband ID'] = line.split()[2].replace('@','')
                    family['Husband Name'] = individuals_id_and_name[family['Husband ID']]
                if 'WIFE' in line.split():
                    family['Wife ID'] = line.split()[2].replace('@','')
                    family['Wife Name'] = individuals_id_and_name[family['Wife ID']]
                if 'CHIL' in line.split():
                    if 'children' in family: 
                        family['children'].append(line.split()[2].replace('@',''))
                    else:
                        family['children'] = []
                        family['children'].append(line.split()[2].replace('@',''))
        else:
            for j in range(i,len(lines)-1):
                line = lines[j]
                level = line[0]
                if 'FAM' in line.split() and level == '0':
                    family['id'] = line.split()[1].replace('@','')
                if 'MARR' in line.split():
                    family['married'] = lines[j+1].split('DATE')[1].replace('\n','')
                if 'DIV' in line.split():
                    family['divorced'] = lines[j+1].split('DATE')[1].replace('\n','')
                if 'HUSB' in line.split():
                    family['Husband ID'] = line.split()[2].replace('@','')
                    family['Husband Name'] = individuals_id_and_name[family['Husband ID']]
                if 'WIFE' in line.split():
                    family['Wife ID'] = line.split()[2].replace('@','')
                    family['Wife Name'] = individuals_id_and_name[family['Wife ID']]
                if 'CHIL' in line.split():
                    if 'children' in family: 
                        family['children'].append(line.split()[2].replace('@',''))
                    else:
                        family['children'] = []
                        family['children'].append(line.split()[2].replace('@',''))

        families.append(family)

    return families

def file_parser(filename):
    (individuals, individuals_id_and_name) = save_ind_data(filename)
    families = save_family_data(filename, individuals_id_and_name)
    individuals = pd.DataFrame(individuals)
    families = pd.DataFrame(families)
    return (individuals, families)

def userstories_sprint1(individuals, families):
    has_unique_ids = userstory_7.unique_ids(individuals, families)
    has_unique_families = userstory_8.unique_families(families)
    return has_unique_ids and has_unique_families

def userstories_sprint2(individuals, families):
    all_legal_marriage = userstory_15.marriage_after_14(individuals, families)
    return all_legal_marriage

def output_data(individuals, families):
    output_excel = filename.strip('.ged') + '.xlsx'
    with pd.ExcelWriter(output_excel) as writer:
        individuals.to_excel(writer, sheet_name="Individuals")
        families.sort_values(by = ['id']).to_excel(writer, sheet_name="Families")

def main():
    (individuals, families) = file_parser(filename)
    sprint1_satisfied = userstories_sprint1(individuals, families)
    sprint2_satisfied = userstories_sprint2(individuals, families)
    output_data(individuals, families)

if __name__ == "__main__":
    main()