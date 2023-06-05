import dash
from dash import html
from multipage_report import MultiPageReport
import os

DOCKER_HOST_IP = os.environ.get('DOCKER_HOST_IP', 'localhost')


app = dash.Dash(__name__)

app = MultiPageReport().generate_multipage_report(app)

if __name__ == '__main__':
    app.run_server(debug=True, host=DOCKER_HOST_IP)
