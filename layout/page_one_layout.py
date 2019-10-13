import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from .navbar_load import navbar
from .dashboard_app_load import app


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
