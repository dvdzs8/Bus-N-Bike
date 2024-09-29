#ChatGPT was used in the making of this code

#CONTROL F YOUR NAME TO FIND TWO DATA SETS OF VALUE

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#stop_name, total_ons, latitude, longitude

#BIKE PLOTTING
bikeTripData = pd.read_csv("tripDataPOGOH.csv")
bikeStationData = pd.read_csv("stationDataPOGOH.csv")

# Count the number of starts and stops at each station
start_counts = bikeTripData.groupby('Start Station Name').size().reset_index(name='Start Count')
end_counts = bikeTripData.groupby('End Station Name').size().reset_index(name='End Count')

# Merge the start and end counts into one DataFrame
station_counts = pd.merge(start_counts, end_counts, left_on='Start Station Name', right_on='End Station Name', how='outer').fillna(0)
station_counts['Total Count'] = station_counts['Start Count'] + station_counts['End Count']

# Merge the station counts with the station points data
bikeStationData = bikeStationData.merge(station_counts[['Start Station Name', 'Total Count']], left_on='Name', right_on='Start Station Name', how='left').sort_values(by='Total Count', ascending=False) #FOR JASON, AIDAN, AND JESS: BIKESTATIONDATA AS ABOVE IS WHAT YOU WANT. IT CONTAINS NAME AND TOTAL COUNT!
print(bikeStationData.head(20))

# Jess adding here:
bikeStationData.to_csv('bike_station_output.csv', index=False)

# Normalize the 'Total Count' for coloring
norm = plt.Normalize(bikeStationData['Total Count'].min(), bikeStationData['Total Count'].max())
colors = plt.cm.coolwarm(norm(bikeStationData['Total Count']))

# Plot the bike stations with color based on frequency of starts/stops
plt.figure(figsize=(12, 7))

# Plot bike stations with color corresponding to total starts and stops
sns.scatterplot(
    x='Longitude',
    y='Latitude',
    data=bikeStationData,
    hue='Total Count',
    palette='coolwarm',  # Color from blue (low count) to red (high count)
    s=15,  # Size of the points
    edgecolor='black'
)

# Add labels and title
plt.title('Bike Station Locations with Start/Stop Frequencies')
plt.xlabel('Longitude')
plt.ylabel('Latitude')


# BUS PLOTTING

# #FAKE BUS DATA TO BE REPLACED BY REAL DATA LATER
# mockBusStopData = {
#     'stop_name': ['7TH AVENUE', 'BIGELOW BLVD', '4TH AVE AT 7TH ST', 'ZUPANIC DR', 'BRUCEWOOD DR AT WEXFORD AVE'],
#     'total_ons': [1, 900, 50, 200, 500],
#     'latitude': [40.44, 40.459, 40.42, 40.4, 40.46],
#     'longitude': [-79.9, -79.97, -80, -79.95, -79.993]
# }

# mockBusStopData = {
#     'stop_name': ['7TH AVENUE', 'BIGELOW BLVD', '4TH AVE AT 7TH ST', 'ZUPANIC DR', 'BRUCEWOOD DR AT WEXFORD AVE','7TH AVENUE', 'BIGELOW BLVD', '4TH AVE AT 7TH ST', 'ZUPANIC DR', 'BRUCEWOOD DR AT WEXFORD AVE'],
#     'total_ons': [1, 900, 50, 200, 500, 7, 7777, 77, 7777, 77],
#     'latitude': [40.44, 40.459, 40.42, 40.4, 40.46, 40.44, 40.459, 40.42, 40.4, 40.46],
#     'longitude': [-79.9, -79.97, -80, -79.95, -79.993,-79.9, -79.97, -80, -79.95, -79.993]
# }

rawBus = pd.read_csv('david_bus.csv')
print(rawBus.head(3))
rawBus = rawBus[rawBus['datekey'] == 201909]
keep_col = ['stop_name','latitude','longitude','total_ons']
colBus = rawBus[keep_col]
colBus.to_csv("cleaned_bus.csv", index=False)

busStopData = colBus.groupby(['stop_name', 'latitude', 'longitude'], as_index=False).sum()
busStopData = busStopData.sort_values('total_ons',ascending=False).head(47).sort_values('total_ons',ascending=True) #AIDAN JASON JESS

# Create DataFrame
bus_df = pd.DataFrame(busStopData)

# Normalize total_ons for color mapping
norm_bus = plt.Normalize(bus_df['total_ons'].min(), bus_df['total_ons'].max())

# Plot the bus stops with color corresponding to total_ons
sns.scatterplot(
    x='longitude',
    y='latitude',
    data=bus_df,
    hue='total_ons',
    palette='coolwarm',  # Color from blue (low count) to red (high count)
    s=50,  # Size of the points
    edgecolor='black'
)

# Add legend for bus stops
plt.legend(title="Bike and Bus Usage")


# Add labels and title
plt.title('Bus Stops and Bike Stations')
plt.xlabel('Longitude')
plt.ylabel('Latitude')


# Show the plot
plt.show()