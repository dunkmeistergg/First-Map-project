import folium

# 1. Create the base map (Light Mode by default)
my_map = folium.Map(location=[48.5, 10.5], zoom_start=7, tiles="OpenStreetMap", control_scale=True)

# Headquarters coordinates
porsche_coords = [48.8350, 9.1526]
bmw_coords = [48.1775, 11.5569]

# 2. Add Porsche HQ Marker
folium.Marker(
    location=porsche_coords,
    popup="<b>Porsche HQ</b><br>Stuttgart",
    icon=folium.Icon(color="red", icon="car", prefix='fa')
).add_to(my_map)

# 3. Add BMW HQ Marker
folium.Marker(
    location=bmw_coords,
    popup="<b>BMW HQ</b><br>Munich",
    icon=folium.Icon(color="blue", icon="car", prefix='fa')
).add_to(my_map)

# 4. Draw a PolyLine (Route between HQs)
folium.PolyLine(
    locations=[porsche_coords, bmw_coords],
    color="black",
    weight=3,
    opacity=0.7,
    dash_array="5, 5",
    tooltip="Direct distance: ~190 km"
).add_to(my_map)

# 5. Draw a Buffer Zone (50 km radius around Munich)
folium.Circle(
    location=bmw_coords,
    radius=50000, # Radius in meters
    color="green",
    fill=True,
    fill_opacity=0.2,
    tooltip="Fast logistics zone (50 km radius)"
).add_to(my_map)

# 6. Add Dark Mode layer and Layer Control tool
folium.TileLayer('cartodbdark_matter', name="Dark Mode").add_to(my_map)
folium.LayerControl().add_to(my_map)

# 7. Save the map to an HTML file
my_map.save("First_map_code.html")
print("Map is ready! Open porsche_bmw_map.html in your browser.")