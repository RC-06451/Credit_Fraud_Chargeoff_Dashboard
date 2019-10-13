import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

navbar = dbc.NavbarSimple(
    children=[
        
        dbc.NavItem(dbc.NavLink("Non-Payer(NP)-Model", href="/page-1"), id="page-1-link"),
        dbc.NavItem(dbc.NavLink("Month Six-Delinquent(M6)-Model", href="/page-2"), id="page-2-link"),
        dbc.NavItem(dbc.NavLink("Non-Payer(NP)-Customer", href="/page-3"), id="page-3-link"),
        dbc.NavItem(dbc.NavLink("Month Six-Delinquent(M6)-Customer", href="/page-4"), id="page-4-link")
    ],
    brand="Subprime E-Financial Corporation",
    brand_href="/",
    color="primary",
    dark=True,
)
