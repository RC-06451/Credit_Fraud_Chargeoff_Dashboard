#
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
import pickle

app = dash.Dash(__name__, external_stylesheets= [dbc.themes.BOOTSTRAP])

app.config.suppress_callback_exceptions = True

app.title='Subprime E-Financial Credit Dashboard'

#image data
image_filename = 'credit_card3.png'

#read in both the simulated non-payer(np) and month six delinquent (m6) customer data
df_np = pd.read_csv('np-sim-data-num-test.csv')
df_m6 = pd.read_csv('m6-sim-data-num-test.csv')
df_np_top5 = pd.read_csv('np-sim-data-top5-out.csv')
df_np_2355 = pd.read_csv('np-sim-data-2355-out.csv')
df_m6_top5 = pd.read_csv('m6-sim-data-top5-out.csv')
df_m6_2355 = pd.read_csv('m6-sim-data-2355-out.csv')


#load trained XGBoost models
pickle_in1 = open("np-xgboost-down-top5-new.pickle","rb")
np_clf_top5 = pickle.load(pickle_in1)

pickle_in2 = open("np-xgboost-down-2355-new.pickle","rb")
np_clf_2355 = pickle.load(pickle_in2)

pickle_in3 = open("m6-xgboost-down-top5-new.pickle","rb")
m6_clf_top5 = pickle.load(pickle_in3)

pickle_in4 = open("m6-xgboost-down-2355-new.pickle","rb")
m6_clf_2355 = pickle.load(pickle_in4)

#predict simulated data
X_name=df_np.iloc[:,1]


#np-top5
X_test=df_np_top5
X_test=X_test.as_matrix()


print ("The length of Xname:\n",len(X_name))

print ("X-test data: \n\n",X_test)
#y_pred_np_top5=np_clf_top5.predict(X_test)
#y_pred_proba_np_top5=np_clf_top5.predict_proba(X_test)

y_pred_np_top5=np_clf_top5.predict(X_test)
y_pred_proba_np_top5=np_clf_top5.predict_proba(X_test)

print ('Probabilities for each customer:/n',X_name,y_pred_proba_np_top5[:,1])

print ("prob for row 1 col 1: ",y_pred_proba_np_top5[1,1])
#print ("Accuracy score:",metrics.accuracy_score(y_test,y_pred))
#print ("F1-score-binary",f1_score(y_test,y_pred))


#np-2355
X_test=df_np_2355
X_test=X_test.as_matrix()


y_pred_np_2355=np_clf_2355.predict(X_test)
y_pred_proba_np_2355=np_clf_2355.predict_proba(X_test)


#m6-top5
X_test=df_m6_top5
X_test=X_test.as_matrix()


y_pred_m6_top5=m6_clf_top5.predict(X_test)
y_pred_proba_m6_top5=m6_clf_top5.predict_proba(X_test)

#m6-2355
X_test=df_m6_2355
X_test=X_test.as_matrix()


y_pred_m6_2355=m6_clf_2355.predict(X_test)
y_pred_proba_m6_2355=m6_clf_2355.predict_proba(X_test)

#dash architecture

navbar = dbc.NavbarSimple(
    children=[
        
        dbc.NavItem(dbc.NavLink("NP-Model", href="/page-1"), id="page-1-link"),
        dbc.NavItem(dbc.NavLink("M6-Model", href="/page-2"), id="page-2-link"),
        dbc.NavItem(dbc.NavLink("NP-Customer", href="/page-3"), id="page-3-link"),
        dbc.NavItem(dbc.NavLink("M6-Customer", href="/page-4"), id="page-4-link")
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
                                    
                                ],
                                'layout': {
                                    
                                    'yaxis': {
                                        'title':'Percentage (%)'
                                    },
                                }
                                    


                            }
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

            



# Update the index
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
    if feature_type=='NP-TOP_5':

        if chart_type=='NP-CLASS':
            return html.Img(src=app.get_asset_url('np-class-imbalance.png'))
        elif chart_type=='NP-FEATURES':
            return html.Img(src=app.get_asset_url('np-f-import-top5-sm.png'))
        elif chart_type=='NP-MODEL_SCORES':
            return html.Img(src=app.get_asset_url('np-model-scores-title.png'))
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
            return html.Img(src=app.get_asset_url('np-model-scores-title.png'))
        elif chart_type=='NP-CONFUSION_MATRIX_RAW':
            return html.Img(src=app.get_asset_url('np-xg-cm-raw-down-2355.png'))
        elif chart_type=='NP-CONFUSION_MATRIX_NORM':
            return html.Img(src=app.get_asset_url('np-xg-cm-norm-down-2355.png'))
        elif chart_type=='NP-ROC':
            return html.Img(src=app.get_asset_url('np-xg-roc-down-2355.png'))
        
        else:
            return html.Img(src=app.get_asset_url('np-natl.png'))
    
     
#callback for choosing M6 model graph/chart
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
            return html.Img(src=app.get_asset_url('m6-model-scores-title.png'))
        elif chart_type=='M6-CONFUSION_MATRIX_RAW':
            return html.Img(src=app.get_asset_url('m6-xg-cm-raw-up-top5.png'))
        elif chart_type=='M6-CONFUSION_MATRIX_NORM':
            return html.Img(src=app.get_asset_url('m6-xg-cm-norm-up-top5.png'))
        elif chart_type=='M6-ROC':
            return html.Img(src=app.get_asset_url('m6-xg-roc-norm-up-top5.png'))
        else:
            return html.Img(src=app.get_asset_url('m6-natl-new.png'))

        
    else: #2355 features 

        if chart_type=='M6-CLASS':
            return html.Img(src=app.get_asset_url('m6-class-imbalance.png'))
        elif chart_type=='M6-FEATURES':
            return html.Img(src=app.get_asset_url('m6-f-import-2355-sm.png'))
        elif chart_type=='M6-MODEL_SCORES':
            return html.Img(src=app.get_asset_url('m6-model-scores-title.png'))
        elif chart_type=='M6-CONFUSION_MATRIX_RAW':
            return html.Img(src=app.get_asset_url('m6-xg-cm-raw-down-2355.png'))
        elif chart_type=='M6-CONFUSION_MATRIX_NORM':
            return html.Img(src=app.get_asset_url('m6-xg-cm-norm-down-2355.png'))
        elif chart_type=='M6-ROC':
            return html.Img(src=app.get_asset_url('m6-roc-down-2355.png'))
        else:
            return html.Img(src=app.get_asset_url('m6-natl-new.png'))
    
     
#callback for choosing NP customer graph/chart
@app.callback(
    Output('np-textarea', 'value'),
    [Input('my-np-customers', 'value'),
     Input('my-np-customer-chart', 'value'),
     
     ])
def update_np_customer(feature_type,chart_type):
    if feature_type=='NP-TOP_5':

        if chart_type=='NP-CUST':
            
            text_risk="*****CUSTOMERS AT-RISK FOR NON-PAYER GROUP*****\n\n"
            text_no_risk="*****CUSTOMERS NOT AT-RISK FOR NON-PAYER GROUP*****\n\n"
            for index in range(1,21):
                if y_pred_np_top5[index-1]:
                    text_risk=text_risk+str(index).rjust(10)+"\t".rjust(10)+str(X_name[index-1]).rjust(20)+str(f'{y_pred_proba_np_top5[index-1,1]:9.4f}').rjust(20)+"\n"
                else:
                    text_no_risk=text_no_risk+str(index).rjust(10)+"\t".rjust(10)+str(X_name[index-1]).rjust(20)+str(f'{y_pred_proba_np_top5[index-1,1]:9.4f}').rjust(20)+"\n"
                
            return text_risk+"\n\n"+text_no_risk
        
        elif chart_type=='NP-LIST':
            text=""
            for index in range(1,21):
                 text=text+str(index).rjust(10)+"\t".rjust(10)+str(X_name[index-1]).rjust(20)+"\n"
                
            return text
       
        else:
            return 'This will hold Nonpayer (NP) customer information'
        
    else: #2355 features 

        if chart_type=='NP-CUST':
            text_risk="*****CUSTOMERS AT-RISK FOR NON-PAYER GROUP*****\n\n"
            text_no_risk="*****CUSTOMERS NOT AT-RISK FOR NON-PAYER GROUP*****\n\n"
            for index in range(1,21):
                if y_pred_np_2355[index-1]:
                    text_risk=text_risk+str(index).rjust(10)+"\t".rjust(10)+str(X_name[index-1]).rjust(20)+str(f'{y_pred_proba_np_2355[index-1,1]:9.4f}').rjust(20)+"\n"
                else:
                    text_no_risk=text_no_risk+str(index).rjust(10)+"\t".rjust(10)+str(X_name[index-1]).rjust(20)+str(f'{y_pred_proba_np_2355[index-1,1]:9.4f}').rjust(20)+"\n"
                
            return text_risk+"\n\n"+text_no_risk
        
        elif chart_type=='NP-LIST':
            text=""
            for index in range(1,21):
                 text=text+str(index).rjust(10)+"\t".rjust(10)+str(X_name[index-1]).rjust(20)+"\n"
                
            return text
        
        else:
            return 'This will hold Nonpayer (NP) customer information'
    

#callback for choosing M6 model graph/chart
@app.callback(
    Output('m6-textarea', 'value'),
    [Input('my-m6-customers', 'value'),
     Input('my-m6-customer-chart', 'value'),
     
     ])
def update_m6_customer(feature_type,chart_type):
    if feature_type=='M6-TOP_5':
        
        if chart_type=='M6-CUST':
            text_risk="*****CUSTOMERS AT-RISK FOR SIX-MONTH DELINQUENT GROUP*****\n\n"
            text_no_risk="*****CUSTOMERS NOT AT-RISK FOR SIX-MONTH DELINQUENT GROUP*****\n\n"
            for index in range(1,21):
                if y_pred_m6_top5[index-1]:
                    text_risk=text_risk+str(index).rjust(10)+"\t".rjust(10)+str(X_name[index-1]).rjust(20)+str(f'{y_pred_proba_m6_top5[index-1,1]:9.4f}').rjust(20)+"\n"
                else:
                    text_no_risk=text_no_risk+str(index).rjust(10)+"\t".rjust(10)+str(X_name[index-1]).rjust(20)+str(f'{y_pred_proba_m6_top5[index-1,1]:9.4f}').rjust(20)+"\n"
                
            return text_risk+"\n\n"+text_no_risk
        elif chart_type=='M6-LIST':
            text=""
            for index in range(1,21):
                 text=text+str(index).rjust(10)+"\t".rjust(10)+str(X_name[index-1]).rjust(20)+"\n"
                
            return text
            
        else:
            return 'This will hold Month Six Delinquent (M6) customer information'

        
    else: #2355 features 

        if chart_type=='M6-CUST':
            text_risk="*****CUSTOMERS AT-RISK FOR SIX-MONTH DELINQUENT GROUP*****\n\n"
            text_no_risk="*****CUSTOMERS NOT AT-RISK FOR SIX-MONTH DELINQUENT GROUP*****\n\n"
            for index in range(1,21):
                if y_pred_m6_2355[index-1]:
                    text_risk=text_risk+str(index).rjust(10)+"\t".rjust(10)+str(X_name[index-1]).rjust(20)+str(f'{y_pred_proba_m6_2355[index-1,1]:9.4f}').rjust(20)+"\n"
                else:
                    text_no_risk=text_no_risk+str(index).rjust(10)+"\t".rjust(10)+str(X_name[index-1]).rjust(20)+str(f'{y_pred_proba_m6_2355[index-1,1]:9.4f}').rjust(20)+"\n"
                
            return text_risk+"\n\n"+text_no_risk
        
        elif chart_type=='M6-LIST':
            text=""
            for index in range(1,21):
                 text=text+str(index).rjust(10)+"\t".rjust(10)+str(X_name[index-1]).rjust(20)+"\n"
                
            return text
        
        else:
            return 'This will hold Month Six Delinquent (M6) customer information'
    

if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0')
