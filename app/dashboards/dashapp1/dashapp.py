from dash import Dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from flask import url_for, redirect

from .. import components

df_iris = px.data.iris()  # iris is a pandas DataFrame

url_base = "/dashboards/iris/"


plot1 = px.density_heatmap(
    df_iris,
    x="sepal_width",
    y="sepal_length",
    marginal_x="rug",
    marginal_y="histogram",
    title="Heatmap",
)
plot3 = px.density_contour(
    df_iris, x="sepal_width", y="sepal_length", title="Density plot"
)
plot4 = px.scatter(
    df_iris,
    x="sepal_length",
    y="sepal_width",
    color="species",
    marginal_x="box",
    marginal_y="violin",
    title="Marginal distribution plots",
)


sample_text = "An early step in any effort to analyze or model data should be to understand how the variables are distributed. Techniques for distribution visualization can provide quick answers to many important questions. What range do the observations cover? What is their central tendency? Are they heavily skewed in one direction? Is there evidence for bimodality? Are there significant outliers? Do the answers to these questions vary across subsets defined by other variables?"


def instanciate(server):
    app = Dash(
        __name__,
        server=server,
        url_base_pathname=url_base,
        external_stylesheets=["/api/static/css/style.css"],
    )

    all_dims = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

    @app.callback(Output("splom", "figure"), [Input("dropdown", "value")])
    def update_bar_chart(dims):
        fig = px.scatter_matrix(
            df_iris,
            dimensions=dims,
            color="species",
            title="Distribution plot with callback",
        )
        return fig

    app.layout = html.Div(
        [
            html.Div(
                components.breadcrumb(
                    [
                        {"text": "home", "link": "/", "class": None},
                        {
                            "text": "Iris Dashboard",
                            "link": "/dashboards/iris",
                            "class": "is-active",
                        },
                    ],
                    container_classes="container is-medium mb-6 pt-5 pb-5",
                ),
                className="has-background-white",
            ),
            html.Div(
                [
                    components.header(
                        title="Iris Dashboard",
                        subtitle="Sample Dashboard using the famous Iris dataset",
                        container_classes="mt-6 mb-5",
                    ),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            dcc.Dropdown(
                                                id="dropdown",
                                                options=[
                                                    {"label": x, "value": x}
                                                    for x in all_dims
                                                ],
                                                value=all_dims[:2],
                                                multi=True,
                                            ),
                                        ],
                                        className="mt-4 mb-1",
                                    ),
                                    dcc.Graph(id="splom"),
                                ],
                                className="column is-12",
                            ),
                            html.Div(
                                [
                                    html.H4(
                                        "Visualizing distributions of data",
                                        className="title is-4 has-text-dark",
                                    ),
                                    html.H5(
                                        "Just a sample text",
                                        className="subtitle is-5 has-text-dark",
                                    ),
                                    html.P(sample_text, className="has-text-white"),
                                ],
                                className="column is-4 mt-3 has-text-justified",
                            ),
                            html.Div(
                                [
                                    dcc.Graph(
                                        id="plot4",
                                        figure=plot4,
                                        config={"displaylogo": False},
                                    )
                                ],
                                className="column is-8",
                            ),
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
                                        id="plot3",
                                        figure=plot3,
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
            ),
            components.footer,
        ]
    )

    return app.server