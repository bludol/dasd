import csv
import json


def load_json_elements(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        groups = json.load(file)
    return groups

def load_csv_elements(csv_file):
    elements = []
    with open(csv_file, 'r', encoding="utf-8") as file:
        csv_txt = csv.reader(file)
        for row in csv_txt:
            elements.append(row)
            csv_row = ",".join(row)
            print(csv_row)
    return elements

groups = load_json_elements('groups.json')
elements = load_csv_elements('elements.csv')
print("\n")
element_to_find ="O"
res1 = any(element_to_find in sublist for sublist in elements)
'''
!!!nutno opravit vyhledavani!!!
for i in range(len(elements[0])):
    index = elements[i].index(element_to_find)
'''


print(res1)
'''
element=[]
for i in range(27):
    element.append(elements[0][i])
print(element)
'''


'''
Možnost vypsat jednotlive sloupce listu elements
Pro vypsani řadku použit : print(elements[J][i])
J = index radku který chceme vypsat. 

i=0 
J=0
for element in elements:
    i+=1
    print(elements[i][J])

'''







