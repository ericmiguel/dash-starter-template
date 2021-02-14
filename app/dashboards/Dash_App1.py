from dash import Dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

url_base = "/dashboards/app1/"

plot1 = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 1, 2])])


def Add_Dash(server):
    app = Dash(
        __name__,
        server=server,
        url_base_pathname=url_base,
        external_stylesheets=["/static/css/style.css"],
    )

    @app.callback(Output("target", "children"), [Input("input-text", "value")])
    def callback_fun(value):
        return "your input is {}".format(value)

    app.layout = html.Div(
        [
            html.Div(
                [
                    html.H1("Hello Dash!", className="title is-2 has-text-primary"),
                    html.Div(
                        [
                            html.Div(
                                [dcc.Input(id="input-text")],
                                className="column is-6",
                            ),
                            html.Div(
                                [html.Div(id="target")], className="column is-6"
                            ),
                            html.Div(
                                [
                                    dcc.Graph(
                                        id="plot1",
                                        figure=plot1,
                                        config={"displaylogo": False},
                                    )
                                ],
                                className="column is-12",
                            ),
                        ],
                        className="columns is-multiline",
                    ),
                ],
                className="container is-max-widescreen",
            )
            # html.Link(rel='stylesheet', href='/static/css/bulma.css'),
            # html.Link(rel='stylesheet', href='/static/css/style.css'),
        ]
    )

    return app.server