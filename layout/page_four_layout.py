import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from .navbar_load import navbar
from .dashboard_app_load import app

page_4_layout = dbc.Container(
   
    [
        navbar,
        dbc.Row(
            [
                
                dbc.Col(
                    [
                        html.H2("Customer Analysis"),
                        html.Div([
                            dcc.RadioItems(
                            id='my-m6-customers',
                            options=[
                            {'label': 'Top 5 Model Features', 'value': 'M6-TOP_5'},
                            {'label': '2355 Model Features', 'value': 'M6-ALL'},
                            ],
                            value='M6-TOP_5'
                         ),
                            html.Div(id='m6-customer-output-container')
                        ]),
                        html.Div([
                            dcc.Dropdown(
                            id='my-m6-customer-chart',
                            options=[
                            {'label': 'Select Option', 'value': 'M6-DEFAULT'},
                            {'label': '-------------M6-CUSTOMER ANALYSIS----------', 'value': 'M6-DEFAULT'},
                            {'label': 'List of Simulated Customers', 'value': 'M6-LIST'},
                            {'label': 'At-Risk M6 Customers', 'value': 'M6-CUST'},
                            
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
                            #html.Div(id='m6-customer-chart-output-container')
                            dcc.Textarea(
                                id='m6-textarea',
                                value='This will hold Month Six Delinquent (M6) customer information',
                                style={'width':'100%', 'height':'400px'}
                            )

                        ]),
                        
                    ]
                ),
            ]
        )
    ],
    className="mt-4",
)
