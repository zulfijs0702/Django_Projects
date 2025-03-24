import dash
from dash import html, dcc
app = dash. Dash(__name__)
app.layout = html.Div([
    html. H1("My Third Dash App"), dcc.Input(placeholder='Enter your text here...')])
if __name__ == '__main__':
    app.run_server (debug=True)