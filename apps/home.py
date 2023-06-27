import streamlit as st
import folium
from streamlit_folium import st_folium
import h3
import branca.colormap as cm
from branca.element import Template, MacroElement

class ColorScaleLegend(MacroElement):
    def __init__(self, color_scale, caption):
        super(ColorScaleLegend, self).__init__()
        self.color_scale = color_scale
        self.caption = caption

        self._template = Template("""
            {% macro html(this, kwargs) %}
            <div style="
                position: fixed;
                bottom: 50px;
                left: 50px;
                width: 200px;
                height: 30px;
                z-index:9999;
                font-size:12px;
                ">
                <div style="background-color: {{this.color_scale}}; width: 100%; height: 100%;">&nbsp;</div>
                <div>{{this.caption}}</div>
            </div>
            {% endmacro %}
        """)

def app():
    st.title("Connect AI")
    st.subheader("Finding you the best place to meet")
    # st.markdown()

    # Base map
    map = folium.Map(location=[1.3521, 103.8198], zoom_start=12, tiles="CartoDB Positron")

    # Color scale for the different time
    color_scale = cm.LinearColormap(['green', 'yellow', 'red', 'purple'], vmin=0, vmax=120)
    # color_scale.caption = 'Time in minutes'
    # color_scale.add_to(map)

    # Hexagon
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
        color = color_scale(time)
        folium.Polygon(
            locations=geo_boundary,
        color=None,
        fill=True,
        fill_color=color,
        fill_opacity=0.6,
        popup=f'Time: {time:.2f} min'
        ).add_to(map)

    legend = ColorScaleLegend(color_scale, "Time in minutes")
    map.get_root().add_child(legend)

    st_folium(map, width=1400, height=700)

if __name__ == "__main__":
    app()
