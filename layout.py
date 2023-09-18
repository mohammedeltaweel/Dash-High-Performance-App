import dash
from dash import html, dcc, Input, Output, callback, clientside_callback, State, Dash, ctx
import dash_bootstrap_components as dbc
import pandas as pd
from dash_svg import Svg, G, Path
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from utils import get_avg_value, get_difference, load_data
# define the main topic
topic = "Connectivity"

# Load the JSON data from the URL
file_path = "data/OutputEPSG4326.geojson"

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Iterate through features and add 'id' field
    for feature in data['features']:
        feature['id'] = feature['properties']['GOVERNORATE_ID']

except Exception as e:
    print(f"An error occurred: {e}")