import yaml
import googlemaps
from datetime import datetime
import pprint
import streamlit as st
import numpy as np


pp = pprint.PrettyPrinter(indent=4)


configs = yaml.load(open("configs/google_api.yaml", "r"))
client_key = configs["client_key"]

def calc_zoom(west_lng, east_lng):
    GLOBE_WIDTH = 256
    angle = east_lng - west_lng
    if angle < 0:
        angle += 360

    zoom = int((np.log(256*360 / angle / GLOBE_WIDTH)/np.log(2))//1)
    return zoom


gmaps = googlemaps.Client(key=client_key)

selection = st.text_input("Select area")

geocode_results = gmaps.geocode(selection)

names = [*map(lambda x: x["formatted_address"], geocode_results)]

st.text(f"Current Selection: {names[0]}")
st.text(f"Other Options: {names[1:]}")

current = geocode_results[0]

coords =  (current["geometry"]["location"]["lat"],
           current["geometry"]["location"]["lng"])


id     =   current["place_id"]

east_lng, west_lng = (current["geometry"]["bounds"]["northeast"]["lng"], current["geometry"]["bounds"]["southwest"]["lng"])
zoom = calc_zoom(west_lng, east_lng)

st.deck_gl_chart( viewport={ 'latitude': coords[0], 'longitude': coords[1], 'zoom': zoom + 2, 'pitch': 50,})

st.json(geocode_results)

