#
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(__name__, external_stylesheets= [dbc.themes.BOOTSTRAP])

app.config.suppress_callback_exceptions = True

app.title='Subprime E-Financial Credit Dashboard'

#image data
image_filename = 'credit_card3.png'

navbar = dbc.NavbarSimple(
    children=[
        
        dbc.NavItem(dbc.NavLink("NP", href="/page-1"), id="page-1-link"),
        dbc.NavItem(dbc.NavLink("M6", href="/page-2"), id="page-2-link")
    ],
    brand="Subprime E-Financial Corporation",
    brand_href="/",
    color="primary",
    dark=True,
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


#index_page = html.Div([
#    navbar,
#    dcc.Graph(
#            figure={"data": [{"x": [1, 2, 3], "y": [10, 2, 3]}]}
#    ),

#])

index_page = dbc.Container(
   
    [
        navbar,
        dbc.Row(
            [
                
                dbc.Col(
                    [
                        html.H2("News"),
                        html.P(
                            """\
Subprime E-Financial Corporation is one of America's leading marketers and servicers of credit cards for consumers with less-than-perfect credit.
"""
                        ),
                        #dbc.Button("View details", color="secondary"),
                        html.Img(src=app.get_asset_url(image_filename)),
                    ],
                    md=4,
                    style={'display':'inline-block'},
                ),
                dbc.Col(
                    [
                        html.H2("Summary Statistics"),
                        dcc.Graph(id='summary-graph',
                            figure={"data": [
                                {'x': ['**NP**','M6'], 'y': [5.2,17.0],'type':'bar','name':'SubPrime'},
                                {'x': ['**NP**','M6'], 'y': [0.0,8.0],'type':'bar','name':'National Avg'},
                                    
                            ]}
                        ),
                    ]
                ),
            ]
        )
    ],
    className="mt-4",
)

page_1_layout = dbc.Container(
   
    [
        navbar,
        dbc.Row(
            [
                
                dbc.Col(
                    [
                        html.H2("Data Analysis"),
                        html.Div([
                            dcc.RadioItems(
                            id='my-np-features',
                            options=[
                            {'label': 'Top 5 Model Features', 'value': 'NP-TOP_5'},
                            {'label': '2355 Model Features', 'value': 'NP-ALL'},
                            ],
                            value='NP-TOP_5',
                         ),
                            html.Div(id='np-features-output-container')
                        ]),
                        html.Div([
                            dcc.Dropdown(
                            id='my-np-chart',
                            options=[
                            {'label': 'Select Option', 'value': 'NP-DEFAULT'},
                            {'label': '-----------NP-MODEL DATA ANALYSIS--------', 'value': 'NP-DEFAULT'},
                            {'label': 'Class Imbalance', 'value': 'NP-CLASS'},
                            {'label': 'Feature Importance ', 'value': 'NP-FEATURES'},
                            {'label': 'Model Scores ', 'value': 'NP-MODEL_SCORES'},
                            {'label': 'Confusion Matrix-Raw Counts', 'value': 'NP-CONFUSION_MATRIX_RAW'},
                            {'label': 'Confusion Matrix-Normalized', 'value': 'NP-CONFUSION_MATRIX_NORM'},
                            {'label': 'Receiver Operating Curve (ROC)', 'value': 'NP-ROC'},
                            ],
                            value='NP-DEFAULT',
                         ),
                        ]),
                        
                        #dbc.Button("View details", color="secondary"),
                    ],
                                 
                    md=4,
                ),
                dbc.Col(
                    [
                        html.H2("N6-Credit Fraud (Non-Payer)"),
                        html.Div([
                        
                            html.Div(id='np-chart-output-container')
                        ])
                    ]
                ),
            ]
        )
    ],
    className="mt-4",
)


#page_1_layout = html.Div([navbar, html.H1('NP'),
#                          dcc.Graph(
#                            figure={"data": [{"x": [1, 2, 3], "y": [1, 4, 9]}]}
#                        ),
#])

page_2_layout = dbc.Container(
   
    [
        navbar,
        dbc.Row(
            [
                
                dbc.Col(
                    [
                        html.H2("Data Analysis"),
                        html.Div([
                            dcc.RadioItems(
                            id='my-m6-features',
                            options=[
                            {'label': 'Top 5 Model Features', 'value': 'M6-TOP_5'},
                            {'label': '2355 Model Features', 'value': 'M6-ALL'},
                            ],
                            value='M6-TOP_5'
                         ),
                            html.Div(id='m6-features-output-container')
                        ]),
                        html.Div([
                            dcc.Dropdown(
                            id='my-m6-chart',
                            options=[
                            {'label': 'Select Option', 'value': 'M6-DEFAULT'},
                            {'label': '-------------M6-MODEL DATA ANALYSIS----------', 'value': 'M6-DEFAULT'},
                            {'label': 'Class Imbalance', 'value': 'M6-CLASS'},
                            {'label': 'Feature Importance ', 'value': 'M6-FEATURES'},
                            {'label': 'Model Scores ', 'value': 'M6-MODEL_SCORES'},
                            {'label': 'Confusion Matrix-Raw Counts', 'value': 'M6-CONFUSION_MATRIX_RAW'},
                            {'label': 'Confusion Matrix-Normalized', 'value': 'M6-CONFUSION_MATRIX_NORM'},
                            {'label': 'Receiver Operating Curve (ROC)', 'value': 'M6-ROC'},
                            
                            ],
                            value='M6-DEFAULT'
                         ),
                            
                        ]),
                        
                        #dbc.Button("View details", color="secondary"),
                    ],
                    md=4,
                ),
                dbc.Col(
                    [
                        html.H2("M6-Six-Month Charge Off Status"),
                        html.Div([
                            html.Div(id='m6-chart-output-container')

                        ]),
                        
                    ]
                ),
            ]
        )
    ],
    className="mt-4",
)


#page_2_layout = html.Div([navbar, html.H1('M6'),
#                           dcc.Graph(
#                            figure={"data": [{"x": [1, 2, 3], "y": [0, 20, 9]}]}
#                        ),
#])
                    



# Update the index
@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    else:
        return index_page
        # You could also return a 404 "URL not found" page here
        

# Update which link is active in the navbar
# If there's lots of pages, we can probably be cleverer about generating
# these functions dynamically.
@app.callback(Output('page-1-link', 'active'), [Input('url', 'pathname')])
def set_page_1_active(pathname):
    return pathname == '/page-1'

    
@app.callback(Output('page-2-link', 'active'), [Input('url', 'pathname')])
def set_page_2_active(pathname):
    return pathname == '/page-2'

#callback for choosing NP graph/chart
@app.callback(
    Output('np-chart-output-container', 'children'),
    [Input('my-np-features', 'value'),
     Input('my-np-chart', 'value'),
     ])
def update_np_graph(feature_type,chart_type):
    if feature_type=='NP-TOP_5':

        if chart_type=='NP-CLASS':
            return html.Img(src=app.get_asset_url('np-class-imbalance.png'))
        elif chart_type=='NP-FEATURES':
            return html.Img(src=app.get_asset_url('np-f-import-top5-sm.png'))
        elif chart_type=='NP-MODEL_SCORES':
            return html.Img(src=app.get_asset_url('np-xg-model-scores.png'))
        elif chart_type=='NP-CONFUSION_MATRIX_RAW':
            return html.Img(src=app.get_asset_url('np-xg-cm-raw-up-top5.png'))
        elif chart_type=='NP-CONFUSION_MATRIX_NORM':
            return html.Img(src=app.get_asset_url('np-xg-cm-norm-up-top5.png'))
        elif chart_type=='NP-ROC':
            return html.Img(src=app.get_asset_url('np-xg-roc-up-top5.png'))
        else:
            return html.Img(src=app.get_asset_url('np-natl.png'))
        
    else: #2355 features 

        if chart_type=='NP-CLASS':
            return html.Img(src=app.get_asset_url('np-class-imbalance.png'))
        elif chart_type=='NP-FEATURES':
            return html.Img(src=app.get_asset_url('np-f-import-2355-sm.png'))
        elif chart_type=='NP-MODEL_SCORES':
            return html.Img(src=app.get_asset_url('np-xg-model-scores.png'))
        elif chart_type=='NP-CONFUSION_MATRIX_RAW':
            return html.Img(src=app.get_asset_url('np-xg-cm-raw-down-2355.png'))
        elif chart_type=='NP-CONFUSION_MATRIX_NORM':
            return html.Img(src=app.get_asset_url('np-xg-cm-norm-down-2355.png'))
        elif chart_type=='NP-ROC':
            return html.Img(src=app.get_asset_url('np-xg-roc-down-2355.png'))
        
        else:
            return html.Img(src=app.get_asset_url('np-natl.png'))
    
     
#callback for choosing M6 graph/chart
@app.callback(
    Output('m6-chart-output-container', 'children'),
    [Input('my-m6-features', 'value'),
     Input('my-m6-chart', 'value'),
     ])
def update_m6_graph(feature_type,chart_type):
    if feature_type=='M6-TOP_5':
        
        if chart_type=='M6-CLASS':
            return html.Img(src=app.get_asset_url('m6-class-imbalance.png'))
        elif chart_type=='M6-FEATURES':
            return html.Img(src=app.get_asset_url('m6-f-import-top5-sm.png'))
        elif chart_type=='M6-MODEL_SCORES':
            return html.Img(src=app.get_asset_url('m6-xg-model-scores.png'))
        elif chart_type=='M6-CONFUSION_MATRIX_RAW':
            return html.Img(src=app.get_asset_url('m6-xg-cm-raw-up-top5.png'))
        elif chart_type=='M6-CONFUSION_MATRIX_NORM':
            return html.Img(src=app.get_asset_url('m6-xg-cm-norm-up-top5.png'))
        elif chart_type=='M6-ROC':
            return html.Img(src=app.get_asset_url('m6-xg-roc-norm-up-top5.png'))
        else:
            return html.Img(src=app.get_asset_url('m6-natl.png'))

        
    else: #2355 features 

        if chart_type=='M6-CLASS':
            return html.Img(src=app.get_asset_url('m6-class-imbalance.png'))
        elif chart_type=='M6-FEATURES':
            return html.Img(src=app.get_asset_url('m6-f-import-2355-sm.png'))
        elif chart_type=='M6-MODEL_SCORES':
            return html.Img(src=app.get_asset_url('m6-xg-model-scores.png'))
        elif chart_type=='M6-CONFUSION_MATRIX_RAW':
            return html.Img(src=app.get_asset_url('m6-xg-cm-raw-down-2355.png'))
        elif chart_type=='M6-CONFUSION_MATRIX_NORM':
            return html.Img(src=app.get_asset_url('m6-xg-cm-norm-down-2355.png'))
        elif chart_type=='M6-ROC':
            return html.Img(src=app.get_asset_url('m6-roc-down-2355.png'))
        else:
            return html.Img(src=app.get_asset_url('m6-natl.png'))
    
     


if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0')
