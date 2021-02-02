import json
import plotly.express as px
filename='eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data=json.load(f)
    
all_eq_dicts=all_eq_data['features'] 
mags,titles,lons,lats=[],[],[],[]

#mags=[]
for eq_dict in all_eq_dicts:
    mag=eq_dict['properties']['mag']
    title=eq_dict['properties']['title']
    lon=eq_dict['geometry']['coordinates'][0]
    lat=eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lats.append(lat)
    lons.append(lon)
fig=px.scatter(
    x=lons,
    y=lats,
    labels={'x':'经度','y':'纬度'},
    range_x=[-200,200],
    range_y=[-90,90],
    width=800,
    height=800,
    title='world earthquake'
    )

fig.write_html('global_earthquakes.html')
fig.show()











