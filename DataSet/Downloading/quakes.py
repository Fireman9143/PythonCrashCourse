from pathlib import Path
import json
import plotly.express as px

path = Path('quake_data/eq_data_30_day_m1.geojson')
contents = path.read_text()
all_data = json.loads(contents)

path = Path('quake_data/readable_eq_data.geojson')
readable = json.dumps(all_data, indent=4)
path.write_text(readable)

all_eq_dicts = all_data['features']
mags, lons, lats, eq_titles = [], [], [], []
for each in all_eq_dicts:
    mag = each['properties']['mag']
    lon = each['geometry']['coordinates'][0]
    lat = each['geometry']['coordinates'][1]
    eq_title = each['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)

title = "Global Earthquakes"
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
                     color=mags,
                     color_continuous_scale='Viridis',
                     labels={'color':'Magnitude'},
                     projection='natural earth',
                     hover_name=eq_titles,
                     )
fig.show()