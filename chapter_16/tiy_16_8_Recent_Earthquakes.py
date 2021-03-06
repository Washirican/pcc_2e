# --------------------------------------------------------------------------- #
# D. Rodriguez, 2020-10-27, File Created.
# --------------------------------------------------------------------------- #

import requests
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Extra credit: Get recent earthquake data from USGS.
request_url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/' \
              '1.0_day.geojson'

response = requests.get(request_url)
recent_eq_data = response.json()

# Explore the structure of the data.
# filename = 'data/my_eq_data_1_day_m1.json'
# with open(filename, 'w') as f:
#     json.dump(recent_eq_data, f)

# readable_file = 'data/readable_eq_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(recent_eq_data, f, indent=4)

# Get chart title from json data
title = recent_eq_data['metadata']['title']

# Extract earthquake dictionaries from json data
all_eq_dicts = recent_eq_data['features']
# print(len(all_eq_dicts))

# Get earthquake magnitudes and store them in a list.
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    # mag = eq_dict['properties']['mag']
    # lon = eq_dict['geometry']['coordinates'][0]
    # lat = eq_dict['geometry']['coordinates'][1]

    # Get additional data from file for hover text.
    # title = eq_dict['properties']['title']

    # Refactor to use values directly and not saving to temporary variables
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# print(mags[:10])
# print(lons[:10])
# print(lats[:10])

# Map the earthquakes.
# data = [Scattergeo(lon=lons, lat=lats)]

# Define chart in a way that is better to customize it.
data = [
    {
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'text': hover_texts,
        'locationmode': 'USA-states',
        'marker': {
            # Define marker size depending on earthquake magnitude.
            'size': [5*mag for mag in mags],

            # Customizing marker colors.
            'color': mags,
            'colorscale': 'Viridis',
            'reversescale': True,
            'colorbar': {'title': 'Magnitude'},
            }
        }
    ]

my_layout = Layout(title=title)
my_layout.geo.update(
        showcountries=True,
        # fitbounds='locations',
        # scope='usa',
        # scope='south america',
        landcolor='rgb(217, 217, 217)',
        )

fig = {
    'data': data,
    'layout': my_layout
    }

offline.plot(fig, filename='global_earthquakes.html')
