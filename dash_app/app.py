import dash
from dash import html , dcc

app  = dash.Dash(__name__, requests_pathname_prefix='/dashboard/')


app.layout = html.Div(children=[
    html.Div([
        html.A('Acceuil',href='/'),
        "|",
        html.A('Logout',href='/logout'),
    ], style={'marginTop':20}),
    
    
    html.H1(children= "Example de Dashboard"),
    
    html.H2(children= "**** Bar Graph ****"),
    dcc.Graph(
        id="exmpl_1",
        figure={
            "data":[
                {"x":[1,2,3] , "y": [6,9,4], "type":"bar", "name":"Example 1" },
                {"x":[7,2,5] , "y": [3,7,1], "type":"bar", "name":"Example 2" }
            ]
        }
    ),
    
    
    html.H2(children= "**** Line Graph ****"),
    dcc.Graph(
        id="exmpl_2",
        figure={
            "data":[
                {"x":[4,3,8] , "y": [4,9,1], "type":"line", "name":"Example 3" },
                {"x":[2,6,8] , "y": [9,6,11], "type":"line", "name":"Example 4" }
            ]
        }
    ),
    
    html.H2(children= "**** Scratter Graph ****"),
    dcc.Graph(
        id="exmpl_3",
        figure={
            "data":[
                {"x":[4,3,8] , "y": [4,9,1], "type":"scatter", "mode":"markers" , "name":"Example 5" },
                {"x":[2,6,8] , "y": [9,6,11], "type":"scatter", "mode":"markers" , "name":"Example 6" }
            ]
        }
    ),
    
        html.H2(children= "**** Pie Chart Graph ****"),
    dcc.Graph(
        id="exmpl_4",
        figure={
            "data":[
                {"labels":["A","B","C"] , "y": [4,9,1], "type":"pie",  "name":"Example 7" },
            ]
        }
    ),
])


server = app.server