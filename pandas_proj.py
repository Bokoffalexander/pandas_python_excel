#!/usr/bin/env python3
# mrcode
import pandas as pd
data = pd.Series([0.25,0.5,0.75,1.0])
print (data)
print (data.values)
print (data.index)
print (data[1])
print (data[1:3])
dataframe = pd.DataFrame(data, columns=['population, k'])
print (dataframe)
exel = pd.read_excel('tmp.xlsx', index_col=0)
