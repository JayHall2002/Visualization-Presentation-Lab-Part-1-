# Import Folium Package and Pandas to Read File
import folium
import pandas as pd

# Load the Downloaded CSV 

data = pd.read_csv('/Users/mighty_jay2002/VisualizationLab1/footprint.csv')

# Create a Base Map
map_college_park = folium.Map(location=[38.989697, -76.937759], zoom_start=13)

# Add Data to the Map

for _, row in data.iterrows():
    folium.CircleMarker(
        location = [row['latitude'], row['longitude']],
        radius = 10,
        color = 'blue',
        fill = True,
        fill_color = 'blue',
        fill_opacity = 0.6
    ).add_to(map_college_park)


# Save file 

map_college_park.save('/Users/mighty_jay2002/VisualizationLab1/college_park_data_map.html')
print("Map has been saved successfully.")
