from dash import Dash

from flask import Flask

import dash_html_components as html

server = Flask(__name__)

dash_app1 = Dash(__name__, server = server, routes_pathname_prefix='/dashboard/' )
dash_app2 = Dash(__name__, server = server, url_base_pathname='/reports/')
dash_app1.layout = html.Div([html.H1('Hi there, I am app1 for dashboards')])
dash_app2.layout = html.Div([html.H1('Hi there, I am app2 for reports')])


@server.route('/')
@server.route('/hello')
def hello():
    return 'hello world!'

# run app on one server
if __name__ == '__main__':
    server.run(debug=True, host='0.0.0.0', port=8080)
