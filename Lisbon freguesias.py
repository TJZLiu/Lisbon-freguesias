import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

old_f= gpd.read_file(r'C:/Users/Desmond/Downloads/data/data/old freguesias/old_freguesias.shp')


current_f = gpd.read_file(r'C:/Users/Desmond/Downloads/data/data/current freguesias/freguesias.shp')

old_f.head(5)

old_f.columns

old_f.iloc[:,:-3]

current_f.iloc[:,:-1]

old_f.plot(edgecolor='black',cmap='hsv',column='NOME')
current_f.plot(edgecolor='black',cmap='hsv',column='Freguesia')