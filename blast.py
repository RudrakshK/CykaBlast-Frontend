import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString, Polygon
import folium
import numpy as np
import flask as Flask


plotholes=pd.read_csv('./templates/potholes.csv.html',index_col=None)
locations=[]
columns=['image','latitude','longitude','depth','width','location','fixed']

for index,row in plotholes.iterrows():     
    location = [float(row[2]), float(row[3])]
    locations+=location
plothole_map = folium.Map(location =[np.mean(location[:][0]),np.mean(location[:][1])] ,zoom_start=16.5)
#create a marker for each school
for index,row in plotholes.iterrows():     
    location = [float(row[2]), float(row[3])] 
    popup_string=''
    for i in range(4,8):
        popup_string+=columns[i-1]+': '+str(row[i])+'<br>'
    popup = folium.Popup(popup_string,max_width=450)
    marker = folium.Marker(location = location, popup=popup)    
    marker.add_to(plothole_map)

plothole_map.save("./templates/my.html")
