#
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
import pickle
from content_load.feature_load import get_data_feature #use one feature function to update all data analysis pages (image objects)
from content_load.feature_customer_load import get_customer_feature #use one feature function to update all customer analysis pages (text objects)


#test os path
#import os
#dirpath=os.getcwd()
#print("current directory is "+dirpath+"\n")

#load dash navbar

from layout.navbar_load import navbar



#dash architecture
#from layout.dashboard_app_load import app
app = dash.Dash(__name__, external_stylesheets= [dbc.themes.BOOTSTRAP])

app.config.suppress_callback_exceptions = True

app.title='Subprime E-Financial Credit Dashboard'

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


#import page layouts
from layout.index_page_layout import index_page
from layout.page_one_layout import page_1_layout
from layout.page_two_layout import page_2_layout
from layout.page_three_layout import page_3_layout
from layout.page_four_layout import page_4_layout


#event callbacks

# Decide which page layout to use
@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    elif pathname == '/page-3':
        return page_3_layout
    elif pathname == '/page-4':
        return page_4_layout
    else:
        return index_page

        
#navigate pages one through four

@app.callback(Output('page-1-link', 'active'), [Input('url', 'pathname')])
def set_page_1_active(pathname):
    return pathname == '/page-1'

    
@app.callback(Output('page-2-link', 'active'), [Input('url', 'pathname')])
def set_page_2_active(pathname):
    return pathname == '/page-2'

@app.callback(Output('page-3-link', 'active'), [Input('url', 'pathname')])
def set_page_3_active(pathname):
    return pathname == '/page-3'

    
@app.callback(Output('page-4-link', 'active'), [Input('url', 'pathname')])
def set_page_4_active(pathname):
    return pathname == '/page-4'

#callback for choosing NP model graph/chart
@app.callback(
    Output('np-chart-output-container', 'children'),
    [Input('my-np-features', 'value'),
     Input('my-np-chart', 'value'),
     
     ])
def update_np_graph(feature_type,chart_type):
    return html.Img(src=app.get_asset_url(get_data_feature(feature_type,chart_type)))



#callback for choosing M6 model graph/chart
@app.callback(
    Output('m6-chart-output-container', 'children'),
    [Input('my-m6-features', 'value'),
     Input('my-m6-chart', 'value'),
     
     ])
def update_m6_graph(feature_type,chart_type):
    return html.Img(src=app.get_asset_url(get_data_feature(feature_type,chart_type)))

     
#callback for choosing NP customer graph/chart
@app.callback(
    Output('np-textarea', 'value'),
    [Input('my-np-customers', 'value'),
     Input('my-np-customer-chart', 'value'),
     
     ])
def update_np_customer(feature_type,chart_type):
   return get_customer_feature(feature_type,chart_type)
    



#callback for choosing M6 model graph/chart
@app.callback(
    Output('m6-textarea', 'value'),
    [Input('my-m6-customers', 'value'),
     Input('my-m6-customer-chart', 'value'),
     
     ])
def update_m6_customer(feature_type,chart_type):
    return get_customer_feature(feature_type,chart_type)
    
    
if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0')
