import streamlit as st
import leafmap.foliumap as leafmap


def app():

    st.title("Heatmap")

    filepath = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/world_cities.csv"
    m = leafmap.Map(tiles="stamentoner")
    m.add_heatmap(
        filepath,
        latitude="latitude",
        longitude="longitude",
        value="pop_max",
        name="Heat map",
        radius=20,
    )
    m.to_streamlit(height=700)
    m = leafmap.Map(center=(1.3521, 103.8198), zoom=12)
