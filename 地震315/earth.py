import json
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
    
print(mags[:10])
print(titles[:2])
print(lons[:5])
print(lats[:5])