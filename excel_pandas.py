#!/usr/bin/env python3
# excel
# find biggest cities
# more than 3 millions
import pandas as pd

# считываем ексель файл
print ("Считываем весь эксель файл:")
excel = pd.read_excel('tmp.xlsx', index_col=None, header=None)
print (excel) # type Series

# население
serie = excel[4]
res = [] # индексы городов более 3 млн
print ("\nНаселение более 3 млн:")
for index, row in serie.items():
    if isinstance(row, str):    
        continue
    if row>3000000:
        print (index," ",row)
        res.append(index)

# города
serie=excel[1]
print ("\nИндексы этих городов:")
print (res) # индексы городов более 3 млн
print ("\nГорода более 3 млн:")
for index, row in serie.items():
    if isinstance(row, str):    
        for x in res:
            if x==index:
                print (index," ",row)
