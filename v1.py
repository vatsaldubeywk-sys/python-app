from dash import Dash, dcc, html, Output, Input
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
server = app.server

app.layout = dbc.Container([
    dcc.Input(id='my_text', type='text', placeholder='Type text now'),
    dcc.Markdown(id='my_output', children='')
])

@app.callback(
    Output('my_output', 'children'),
    Input('my_text', 'value')
)
def update_output(el_texto):
    return el_texto

if __name__ == '__main__':
    app.run(debug=True)