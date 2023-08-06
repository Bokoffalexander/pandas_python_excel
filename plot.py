# coding: utf-8
import pandas as pd
get_ipython().run_line_magic('pip', 'install pandas-datareader')
from pandas_datareader import data
goog = data.DataReader('GOOG',start='2004', end='2022',data_source='google')
goog = data.DataReader('GOOG', start='2004', end='2022', data_source='google')
goog = data.DataReader('GOOG', start='2004', end='2022', data_source='google')
goog = data.DataReader('GOOG', start='2004', end='2022', data_source='yahoo')
df = pd.DataFrame({'lab':['A', 'B', 'C'], 'val':[10, 30, 20]})
ax = df.plot.bar(x='lab', y='val', rot=0)01~
ax = df.plot.bar(x='lab', y='val', rot=0)
ax = df.plot.bar(x='lab', y='val', rot=0)
get_ipython().run_line_magic('pip', 'install matplotlib')
ax = df.plot.bar(x='lab', y='val', rot=0)
get_ipython().run_line_magic('ls', '')
df.plot.bar(x='lab', y='val', rot=0) > plot
df.plot.bar(x='lab', y='val', rot=0) > plot
ax.savefig('saved_figure.png')
df = pd.DataFrame({'lab':['A', 'B', 'C'], 'val':[10, 30, 20]})
ax = df.plot.bar(x='lab', y='val', rot=0)01~
ax = df.plot.bar(x='lab', y='val', rot=0)
ax.savefig('saved_figure.png')
import matplotlib.pyplot as plt
plt.savefig('saved_figure.png')
get_ipython().run_line_magic('ls', '')
