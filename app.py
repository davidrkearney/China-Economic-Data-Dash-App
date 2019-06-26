import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://gist.githubusercontent.com/davidrkearney/d9dfeb184b44367ff79dd75f69e672dd/raw/8175d1dd1d0b9d21b6469e7a22acb54faca38e1f/plot_css.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv(
    'https://gist.githubusercontent.com/davidrkearney/' +
    'bb461ba351da484336a19bd00a2612e2/raw/18dd90b57fec46a247248d161ffd8085de2a00db/' +
    '/china_province_economicdata_1996_2007.csv')



app.layout = html.Div([
    dcc.Graph(
        id='GDP per capita across regions of China',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['Region'] == i]['Year'],
                    y=df[df['Region'] == i]['gdp'],
                    text=df[df['Region'] == i]['Province2'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.Region.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'Year'},
                yaxis={'title': 'GDP per capita'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
