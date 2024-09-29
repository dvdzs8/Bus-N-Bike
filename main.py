#using POGOH trip data from March 2024

import pandas as pd
import numpy as np 
import csv

# cleaning data

def clean(fn):
    with open(fn, 'r') as file:
        vsc = pd.read_csv(fn)
        
        vsc = vsc[vsc['Closed Status'] == 'NORMAL']
        keep_col = ['_id','Duration','Start Station Id','Start Date','Start Station Name', 'End Date', 'End Station Id', 'End Station Name']
        new_data = vsc[keep_col]
        new_data.to_csv("cleaned_bike.csv", index=False)


# remove the 'Closed Status' and 'Ride Typer' cols

clean('trip_032024.csv')
data = pd.read_csv('cleaned_bike.csv')

station = data['Start Station Name'].unique()
print(len(station))

uses_sum = []

for x in station:
    if not type(x) == float:
        temp = (data['Start Station Name'] == x).sum()
        uses_sum.append({x, temp})

print(uses_sum)
print(len(uses_sum))






