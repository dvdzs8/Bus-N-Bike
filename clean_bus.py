#using Bus trip data from September 2019

import pandas as pd
import numpy as np 
import csv

# cleaning data

def clean(fn):
    with open(fn, 'r') as file:
        vsc = pd.read_csv(fn)
        vsc = vsc[vsc['datekey'] == 201909]
        keep_col = ['_id','stop_name','latitude','longitude','total_ons']
        new_data = vsc[keep_col]
        new_data.to_csv("cleaned_bus.csv", index=False)

# remove the 'Closed Status' and 'Ride Typer' cols

clean('bus.csv')
data = pd.read_csv('cleaned_bus.csv')

# merge multiple sets?????

station = data['stop_name'].unique()
ons_sum = dict()

for x in station:
    if not type(x) == float:
        temp = data[data['stop_name'].str.contains(x, regex = False)]
        tot = int(temp['total_ons'].sum())
        ons_sum.update({x : tot})

print(ons_sum)

# Analyze blah blah







