import folium
import pandas as pd  # Importing pandas and giving it an alias 'pd' for ease of use

# Load the data from the Excel file
data = pd.read_excel("iit_data.xlsx")

# Extract relevant columns from the DataFrame
iit_ranking = list(data["IIT Ranking"])
college_name = list(data["IIT College"])
nirf_score = list(data["NIRF Score"])
lat = list(data["Latitude"])
lon = list(data["Longitude"])
images = list(data["Image"])

# Create a FeatureGroup for the map
fg = folium.FeatureGroup("map")

# Add a GeoJson layer to the map (for the state boundaries of India)
fg.add_child(folium.GeoJson(data=open("india_states.json", "r", encoding="utf-8-sig").read()))

# Loop through the data and add markers to the map
for rank, name, score, lati, longi, img in zip(iit_ranking, college_name, nirf_score, lat, lon, images):
    popup_content = (
        f"<b>College Name:</b> {name}<br>"
        f"<b>Rank among IIT in India:</b> {rank}<br>"
        f"<b>NIRF Score:</b> {score}<br>"
        f'<img src="{img}" height="145" width="300">'
    )
    # Add a marker for each IIT
    fg.add_child(folium.Marker(location=[lati, longi], 
                               popup=popup_content, 
                               icon=folium.Icon(color="red")))

# Create the map centered on India
map = folium.Map(location=[20.0000, 75.0000], zoom_start=4)

# Add the FeatureGroup to the map
map.add_child(fg)

# Save the map as an HTML file
map.save("sample.html")
