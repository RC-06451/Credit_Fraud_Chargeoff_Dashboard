import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from .navbar_load import navbar
from .dashboard_app_load import app

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
