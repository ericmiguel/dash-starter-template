import dash_html_components as html

def header(title: str, subtitle: str, container_classes: str = None):
    return html.Div(
        [
            html.H1(title, className="title is-2 has-text-white"),
            html.H3(
                subtitle,
                className="subtitle has-text-white",
            ),
        ],
        className=container_classes,
    )
