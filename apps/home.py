import streamlit as st
import leafmap.foliumap as leafmap
from h3 import h3

def app():
    st.title("Connect AI")

    # st.header("Testing Header")

    st.subheader("""
    An app to showcase the best connectivity nearest to you.
    """
    )

    # st.markdown()

    m = leafmap.Map(locate_control=True)
    m.add_basemap("ROADMAP")
    m = leafmap.Map(center=(1.3521, 103.8198), zoom=12)
    m.to_streamlit(height=700)
