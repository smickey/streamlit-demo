import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("Connect AI")

    st.markdown(
        """
    A [streamlit](https://streamlit.io) app to showcase the heatmap connectivity near you.
    """
    )

    m = leafmap.Map(locate_control=True)
    m.add_basemap("ROADMAP")
    m = leafmap.Map(center=(1.3521, 103.8198), zoom=12)
    m.to_streamlit(height=700)
