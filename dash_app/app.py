import dash
from dash import html, dcc
import requests

app = dash.Dash(__name__, requests_pathname_prefix='/dashboard/')

EXTERNAL_API_URL = "https://meteoapi-bsabg6c4aaaqc2h9.canadaeast-01.azurewebsites.net/info"

def get_external_info():
    try:
        response = requests.get(EXTERNAL_API_URL)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("error de api extern:", e)
        return {
            "date": "N/A",
            "time": "N/A",
            "weather": {
                "city": "N/A",
                "temperature": "N/A",
                "description": "N/A"
            }
        }

info = get_external_info()

# Layout du dashboard avec les informations météo
app.layout = html.Div(children=[
    
    html.Div([
        html.A('Accueil', href='/'),
        " | ",
        html.A('Logout', href='/logout'),
    ], style={'marginTop': 20, 'marginBottom': 20}),

    html.H1(children="Exemple de Dashboard"),
    
    
    html.Div([
        html.H2(f"Aujourd'hui est {info['date']} et il est {info['time']}", 
                style={'color': '#2c3e50', 'marginBottom': 20}),
        
        html.Div([
            html.P(f"Ville : {info['weather'].get('city', 'N/A')}", 
                   style={'fontSize': 16, 'margin': '5px 0'}),
            html.P(f"Température : {info['weather'].get('temperature', 'N/A')}", 
                   style={'fontSize': 16, 'margin': '5px 0'}),
            html.P(f"Description : {info['weather'].get('description', 'N/A')}", 
                   style={'fontSize': 16, 'margin': '5px 0'}),
        ], style={
            'backgroundColor': '#f8f9fa',
            'padding': '20px',
            'borderRadius': '8px',
            'border': '1px solid #dee2e6',
            'marginBottom': '30px'
        })
    ], className='info-box'),
    
    # Graphiques existants
    html.H2(children="**** Bar Graph ****"),
    dcc.Graph(
        id="exmpl_1",
        figure={
            "data": [
                {"x": [1, 2, 3], "y": [6, 9, 4], "type": "bar", "name": "Example 1"},
                {"x": [7, 2, 5], "y": [3, 7, 1], "type": "bar", "name": "Example 2"}
            ]
        }
    ),
    
    html.H2(children="**** Line Graph ****"),
    dcc.Graph(
        id="exmpl_2",
        figure={
            "data": [
                {"x": [4, 3, 8], "y": [4, 9, 1], "type": "line", "name": "Example 3"},
                {"x": [2, 6, 8], "y": [9, 6, 11], "type": "line", "name": "Example 4"}
            ]
        }
    ),
    
    html.H2(children="**** Scatter Graph ****"),
    dcc.Graph(
        id="exmpl_3",
        figure={
            "data": [
                {"x": [4, 3, 8], "y": [4, 9, 1], "type": "scatter", "mode": "markers", "name": "Example 5"},
                {"x": [2, 6, 8], "y": [9, 6, 11], "type": "scatter", "mode": "markers", "name": "Example 6"}
            ]
        }
    ),
    
    html.H2(children="**** Pie Chart Graph ****"),
    dcc.Graph(
        id="exmpl_4",
        figure={
            "data": [
                {"labels": ["A", "B", "C"], "values": [4, 9, 1], "type": "pie", "name": "Example 7"},
            ]
        }
    ),
])

server = app.server