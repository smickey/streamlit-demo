import streamlit as st
import leafmap.foliumap as leafmap
import folium
from streamlit_folium import st_folium, folium_static
from h3 import h3

def app():
    st.title("Connect AI")
    st.markdown(
        """
        Welcome to Connect AI!
        """
    )
    map = folium.Map(location=[1.3521, 103.8198], zoom_start=12, tiles="CartoDB Positron")
    hexagons = {
        '8a652636062ffff': 0,
        '8a6526360197fff': 11.600000000000001,
        '8a652636051ffff': 13.700000000000001,
        '8a6526360777fff': 3.7096248711548725,
        '8a6526360767fff': 7.340706024792129,
        # Add more hexagons here...
    }
    for h3_index, time in hexagons.items():
        geo_boundary = h3.h3_to_geo_boundary(h3_index, geo_json=False)
        folium.Polygon(
            locations=geo_boundary,
            fill=True,
            fill_opacity=0.6,
        ).add_to(map)
    st_folium(map, width=700, height=700)
if __name__ == "__main__":
    app()

# def app():
#     st.title("Connect AI")

#     # st.header("Testing Header")

#     st.subheader("""
#     An app to showcase the best connectivity nearest to you.
#     """
#     )

#     # st.markdown()

#     m = leafmap.Map(locate_control=True)
#     m.add_basemap("ROADMAP")
#     m = leafmap.Map(center=(1.3521, 103.8198), zoom=12)
#     m.to_streamlit(height=700)
