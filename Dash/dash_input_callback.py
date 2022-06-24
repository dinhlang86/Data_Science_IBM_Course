from statistics import mode
from matplotlib.pyplot import title
import pandas as pd
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Read the airline data into pandas dataframe
airline_data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv',
                           encoding="ISO-8859-1",
                           dtype={'Div1Airport': str, 'Div1TailNum': str,
                                  'Div2Airport': str, 'Div2TailNum': str})

app = dash.Dash(__name__)
app.layout = html.Div(children=[html.H1('Airline Performance Dashboard', style={'textAlign': 'center',
                                                                                'color': '#503D36',
                                                                                'font-size': 40}),
                                html.Div(['Input year ', dcc.Input(id='input-year', type='number', value='2010', style={'fontSize': 35, 'height': '50px'}), ],
                                         style={'fontSize': 40}),
                                html.Br(),
                                html.Br(),
                                html.Div(dcc.Graph(id='line-plot')), ])

# add callback decorator


@app.callback(Output(component_id='line-plot', component_property='figure'), Input(component_id='input-year', component_property='value'))
# Add computation to callback function and return graph
def get_graph(enteredYear):
    # Select data based on the entered year
    df = airline_data[airline_data['Year'] == int(enteredYear)]
    # Group the data by Month and compute average over arrival delay time.
    line_data = df.groupby('Month')['ArrDelay'].mean().reset_index()
    fig = go.Figure(data=go.Scatter(
        x=line_data['Month'], y=line_data['ArrDelay'], mode='lines', marker=dict(color='green')))
    fig.update_layout(title='Month vs Average Flight Delay Time',
                      xaxis_title='Month', yaxis_title='ArrDelay')
    return fig


if __name__ == '__main__':
    app.run_server()
