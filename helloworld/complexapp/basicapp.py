import os
import dash
import dash_core_components as dcc
import dash_html_components as html


basicapp = dash.Dash(__name__)
server = basicapp.server


basicapp.layout = html.Div([
    html.H2('Hello World'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Div(id='display-value')
])

basicapp.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})


@basicapp.callback(dash.dependencies.Output('display-value', 'children'), [dash.dependencies.Input('dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)


if __name__ == '__main__':
    basicapp.run_server(debug=True)
