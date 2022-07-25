import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#Analiza struktury danych
filename = "JSON_excercise/data/eq_data_30_day_m1.json"
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
main_title = all_eq_data['metadata']['title']

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

#Mapa trzęsień ziemi.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Siła'}
    }
}]
my_layout = Layout(title=main_title)

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="global_earthquakes.html")