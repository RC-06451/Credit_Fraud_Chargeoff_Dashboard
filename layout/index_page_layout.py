import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from .navbar_load import navbar
from .dashboard_app_load import app

#image data
image_filename = 'credit_card3.png'

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
                        html.P(
                            """\
KEY TERMS:         """
                        ),
                        html.P(
                            """\
           (1) NP= Non Payer or fraudulent credit transaction--a customer that was approved for a credit card, maxed out the limit but then never made a single payment.
           """
                        ),
                        html.P(
                            """\
           (2) M6= Month Six Delinquent--a customer that has made at least one single payment but then has been delinquent for six months.  At that point in time, they are charged off
           the company books and are put in charge-off status."""
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
                                {'x': ['**NP**','M6'], 'y': [4.0,8.0],'type':'bar','name':'National Avg'},
                                    
                                ],
                                'layout': {
                                    #go.Layout(
                                   # paper_bgcolor='rgba(0,0,0,0)',
                                   # plot_bgcolor='rgba(0,0,0,0)',
                                  #  font=dict(color='white')
                                   # )

                                    
                                    'yaxis': {
                                        'title':'Percentage (%)'
                                    },
                                    'paper_bgcolor':'rgba(0,0,0,0)',
                                    'plot_bgcolor':'rgba(0,0,0,0)',
                                    'font':{
                                        'color':'white'

                                        }
                                    
                                }
                                    


                            }
                        ),
                        html.P(
                            """\
**Note:  The national average for the non-payer,fraudulent (NP) category is an estimate.**"""
                        ),
                        
                    ]
                ),
            ]
        )
    ],
    className="mt-4",
)
