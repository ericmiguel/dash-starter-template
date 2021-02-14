import dash_html_components as html

def breadcrumb(links: list, container_classes: str = None):
    li_items = [html.Li(html.A(item['text'], href=item['link'], className=item['class'])) for item in links]
    breadcrumb_classes = f"breadcrumb {container_classes}"
    return html.Nav([html.Ul(li_items)], className=breadcrumb_classes)
