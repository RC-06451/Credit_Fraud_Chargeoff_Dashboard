import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from .navbar_load import navbar
from .dashboard_app_load import app


page_3_layout = dbc.Container(
   
    [
        navbar,
        dbc.Row(
            [
                
                dbc.Col(
                    [
                        html.H2("Customer Analysis"),
                        html.Div([
                            dcc.RadioItems(
                            id='my-np-customers',
                            options=[
                            {'label': 'Top 5 Model Features', 'value': 'NP-TOP_5'},
                            {'label': '2355 Model Features', 'value': 'NP-ALL'},
                            ],
                            value='NP-TOP_5',
                         ),
                            html.Div(id='np-customer-output-container')
                        ]),
                        html.Div([
                            dcc.Dropdown(
                            id='my-np-customer-chart',
                            options=[
                            {'label': 'Select Option', 'value': 'NP-DEFAULT'},
                            {'label': '-----------NP-CUSTOMER ANALYSIS--------', 'value': 'NP-DEFAULT'},
                            {'label': 'List of Simulated Customers', 'value': 'NP-LIST'},
                            {'label': 'At-Risk NP Customers', 'value': 'NP-CUST'},
                            
                            
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
                        
                           # html.Div(id='np-customer-chart-output-container')
                            dcc.Textarea(
                                id='np-textarea',
                                value='This will hold Nonpayer (NP) customer information',
                                style={'width':'100%', 'height':'400px'}
                            )
                        ])
                    ]
                ),
            ]
        )
    ],
    className="mt-4",
)

