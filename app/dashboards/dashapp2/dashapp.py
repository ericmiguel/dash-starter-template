from dash import Dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px

df = px.data.iris()  # iris is a pandas DataFrame


url_base = "/dashboards/app2/"

plot1 = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 1, 2])])
plot2 = px.scatter(df, x="sepal_width", y="sepal_length")

def instanciate(server):
    app = Dash(
        __name__,
        server=server,
        url_base_pathname=url_base,
        external_stylesheets=["/api/static/css/style.css"],
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
                            html.Div([html.Div(id="target")], className="column is-6"),
                            html.Div(
                                [
                                    dcc.Graph(
                                        id="plot1",
                                        figure=plot1,
                                        config={"displaylogo": False},
                                    )
                                ],
                                className="column is-6",
                            ),
                            html.Div(
                                [
                                    dcc.Graph(
                                        id="plot2",
                                        figure=plot2,
                                        config={"displaylogo": False},
                                    )
                                ],
                                className="column is-6",
                            ),
                        ],
                        className="columns is-multiline",
                    ),
                ],
                className="container is-max-fullhd",
            )
        ]
    )

    return app.server