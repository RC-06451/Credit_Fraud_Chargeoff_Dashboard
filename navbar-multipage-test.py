#
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(__name__, external_stylesheets= [dbc.themes.BOOTSTRAP])

app.config.suppress_callback_exceptions = True

navbar = dbc.NavbarSimple(
    children=[
        
        dbc.NavItem(dbc.NavLink("NP", href="/page-1"), id="page-1-link"),
        dbc.NavItem(dbc.NavLink("M6", href="/page-2"), id="page-2-link")
    ],
    brand="Continental Finance LLC",
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
Founded in 2005, Continental Finance Company ("CFC") is one of America's leading marketers and servicers of credit cards for consumers with less-than-perfect credit. Since the Company's founding, CFC has prided itself on its corporate responsibility to customers in terms of a strong customer support program, fair treatment, and responsible lending.
"""
                        ),
                        dbc.Button("View details", color="secondary"),
                    ],
                    md=4,
                ),
                dbc.Col(
                    [
                        html.H2("Summary Statistics"),
                        dcc.Graph(
                            figure={"data": [{"x": [1, 2, 3], "y": [10, 4, 9]}]}
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
                        html.H2("News"),
                        html.P(
                            """\
Donec id elit non mi porta gravida at eget metus.
Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum
nibh, ut fermentum massa justo sit amet risus. Etiam porta sem
malesuada magna mollis euismod. Donec sed odio dui. Donec id elit non
mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus
commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit
amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed
odio dui."""
                        ),
                        dbc.Button("View details", color="secondary"),
                    ],
                    md=4,
                ),
                dbc.Col(
                    [
                        html.H2("N6"),
                        dcc.Graph(
                            figure={"data": [{"x": [1, 2, 3], "y": [1, 4, 9]}]}
                        ),
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
                        html.H2("News"),
                        html.P(
                            """\
Donec id elit non mi porta gravida at eget metus.
Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum
nibh, ut fermentum massa justo sit amet risus. Etiam porta sem
malesuada magna mollis euismod. Donec sed odio dui. Donec id elit non
mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus
commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit
amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed
odio dui."""
                        ),
                        dbc.Button("View details", color="secondary"),
                    ],
                    md=4,
                ),
                dbc.Col(
                    [
                        html.H2("M6"),
                        dcc.Graph(
                            figure={"data": [{"x": [1, 2, 3], "y": [0, 20, 9]}]}
                        ),
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


if __name__ == '__main__':
    app.run_server(debug=True)
