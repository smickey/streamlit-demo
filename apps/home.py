import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("Connect AI")

    st.markdown(
        """
    A [streamlit](https://streamlit.io) app template for geospatial applications based on [streamlit-option-menu](https://github.com/victoryhb/streamlit-option-menu).
    To create a direct link to a pre-selected menu, add `?page=<app name>` to the URL, e.g., `?page=upload`.
    https://share.streamlit.io/giswqs/streamlit-template?page=upload

    """
    )

    m = leafmap.Map(locate_control=True)
    m.add_basemap("ROADMAP")
    m = leafmap.Map(center=(1.3521, 103.8198), zoom=12)
    m.to_streamlit(height=700)
