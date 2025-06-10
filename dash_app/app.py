import dash
from dash import html , dcc
 
app  = dash.Dash(__name__, requests_pathname_prefix='/dashboard/')
 
 
app.layout = html.Div(children=[
    html.Div([
        html.A('Home',href='/'),
        "|",
        html.A('Logout',href='/logout')
    ], style={'marginTop':20}),
   
   html.H1(children="Exemple de Dashboard"),
    dcc.Graph(
        id="exmpl_1",
        figure={
            "data":[
                {"x":[1,2,3] , "y": [6,9,4], "type":"bar", "name":"Example 1" },
                {"x":[7,2,5] , "y": [3,7,1], "type":"bar", "name":"Example 2" }
            ]
        }
    ),
    html.H2(children="*****Line graph*******"),
    dcc.Graph(
        id="exmpl_2",
        figure={
            "data":[
                {"x":[4,5,6] , "y": [7,8,4+3], "type":"line", "name":"Example 3" },
                {"x":[7,2,5] , "y": [3,7,1], "type":"line", "name":"Example 4" }
            ]
        }
    ),  
    html.H2(children="*****Scatter graph*******"),
   
    dcc.Graph(
        id="exmpl_3",
        figure={
            "data":[
                {"x":[4,5,6] , "y": [7,8,3], "type":"Scatter", "name":"Example 5" },
                {"x":[7,2,5] , "y": [3,7,1], "type":"Scatter", "name":"Example 6" }
            ]
        }
    ),
     html.H2(children="*****pie char graph*******"),
    dcc.Graph(
        id="exmpl_4",
        figure={
            "data":[
                {"labels":["A","B","C"] , "y": [7,8,4], "type":"line", "name":"Example 7" },
               
            ]
        }
    ),
])
 
 
server = app.server