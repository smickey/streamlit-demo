import streamlit as st
import leafmap.foliumap as leafmap
from streamlit_folium import st_folium
from h3 import h3
import folium

def app(hexagons, color="red", folium_map=None):
    """
    hexagons is a list of hexcluster. Each hexcluster is a list of hexagons.
    eg. [[hex1, hex2], [hex3, hex4]]
    """
    polylines = []
    lat = []
    lng = []
    for hex in hexagons:
        polygons = h3.h3_set_to_multi_polygon([hex], geo_json=False)
        # flatten polygons into loops.
        outlines = [loop for polygon in polygons for loop in polygon]
        polyline = [outline + [outline[0]] for outline in outlines][0]
        lat.extend(map(lambda v:v[0],polyline))
        lng.extend(map(lambda v:v[1],polyline))
        polylines.append(polyline)

    if folium_map is None:
        m = folium.Map(location=[sum(lat)/len(lat), sum(lng)/len(lng)], zoom_start=13, tiles='cartodbpositron')
    else:
        m = folium_map
    for polyline in polylines:
        my_PolyLine=folium.Polygon(locations=polyline,fill=True, fill_color=color, fill_opacity=0.3, color=None)
        m.add_child(my_PolyLine)
    # return m
    return st_folium(m, width=725)

# def visualize_polygon(polyline, color):
#     polyline.append(polyline[0])
#     lat = [p[0] for p in polyline]
#     lng = [p[1] for p in polyline]
#     m = folium.Map(location=[sum(lat)/len(lat), sum(lng)/len(lng)], zoom_start=13, tiles='cartodbpositron')
#     my_PolyLine=folium.PolyLine(locations=polyline,weight=8,color=color)
#     m.add_child(my_PolyLine)
#     # return m
#     return st_folium(m, width=725)
