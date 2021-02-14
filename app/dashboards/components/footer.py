import dash_html_components as html


footer = html.Footer(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    ["Hello!"],
                                    className="title is-4 has-text-grey-dark",
                                ),
                                html.Div(
                                    "Vestibulum venenatis vulputate dui et rhoncus. Nullam mauris justo, semper a consequat in, rhoncus ut ex. Quisque viverra nisi vitae dignissim auctor. Mauris mattis non magna sed fringilla. Nullam pulvinar eu quam eu tincidunt. Aenean ut dapibus mi, ultrices mollis est. Aliquam dapibus dolor magna, sed vulputate ante lacinia faucibus. Morbi a efficitur diam.",
                                    className="has-text-justified",
                                ),
                            ],
                            className="column is-6-desktop is-12-mobile has-text-grey-dark",
                        )
                    ],
                    className="columns is-multiline",
                )
            ],
            className="container",
        )
    ],
    className="footer has-background-white mt-6",
    style={"padding": "7rem 0rem 5rem"}
)