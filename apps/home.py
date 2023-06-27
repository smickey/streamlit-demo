import streamlit as st
import folium
from streamlit_folium import st_folium
import h3
import branca.colormap as cm
from branca.element import Template, MacroElement
import requests

@st.cache(allow_output_mutation=True)
def app():
    st.title("Connect AI")
    st.subheader("Finding you the best place to meet")

     # Call API
    response = requests.get(f"https://connectai-emwgdoqmma-de.a.run.app/traveltimeh3?locations={user_input}")
    if response.status_code == 200:
        hex_data = response.json()
    else:
        st.write("Error:", response.status_code)
    hexagons = {}
    for key, value in hex_data.items():
        hexagon_id = list(value.keys())[0]
        measurement = list(value.values())[0]
        hexagons[hexagon_id] = measurement

    # Plot map
    map = folium.Map(location=[1.3521, 103.8198], zoom_start=12, tiles="CartoDB Positron")

    # Add click event handler
    map.add_child(folium.LatLngPopup())
    color_scale = cm.LinearColormap(['green', 'yellow', 'red', 'purple'], vmin=0, vmax=120)
    for h3_index, time in hexagons.items():
        geo_boundary = h3.h3_to_geo_boundary(h3_index, geo_json=False)
        color = color_scale(time)
        folium.Polygon(
            locations=geo_boundary,
        color=None,
        fill=True,
        fill_color=color,
        fill_opacity=0.6,
        popup=f'Time: {time:.2f} min'
        ).add_to(map)
    st_folium(map, width=1400, height=700)

if __name__ == "__main__":
    app()
