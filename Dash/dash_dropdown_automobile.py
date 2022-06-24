import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Output, Input, State
from dash import no_update


# Add Dataframe
auto_data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv',
                        encoding="ISO-8859-1")


app = dash.Dash(__name__)

# REVIEW1: Clear the layout and do not display exception till callback gets executed
app.config.suppress_callback_exceptions = True


# app.layout = html.Div(children=[
#     html.H1(
#         children='Dashboard',
#         style={
#             'textAlign': 'center'
#         }
#     ),

#     # Create dropdown
#     dcc.Dropdown(options=[
#         {'label': 'New York City', 'value': 'NYC'},
#         {'label': 'Montréal', 'value': 'MTL'},
#         {'label': 'San Francisco', 'value': 'SF'}
#     ],
#         value='NYC'  # Providing a vallue to dropdown
#     ),
#     dcc.Graph(id='example-graph-2', figure=fig)
# ])

app.layout = html.Div(children=[html.H1('Car Automobile Components',
                                style={'textAlign': 'center', 'color': '#503D36',
                                       'font-size': 24}),

                                # outer division starts
                                html.Div([
                                    # First inner divsion for  adding dropdown helper text for Selected Drive wheels
                                    html.Div([
                                        html.H2('Drive Wheels Type:', style={'margin-right': '2em'}), ]),
                                    dcc.Dropdown(
                                        id='demo-dropdown',
                                        options=[
                                            {'label': 'Rear Wheel Drive',
                                                'value': 'rwd'},
                                            {'label': 'Front Wheel Drive',
                                                'value': 'fwd'},
                                            {'label': 'Four Wheel Drive',
                                                'value': '4wd'}
                                        ],
                                        value='rwd'
                                    ),

                                    # Second Inner division for adding 2 inner divisions for 2 output graphs
                                    html.Div([
                                        html.Div([], id='plot1'),
                                        html.Div([], id='plot2')
                                    ], style={'display': 'flex'}),


                                ])
                                # outer division ends

                                ])

# Place to add @app.callback Decorator


@app.callback([Output(component_id='plot1', component_property='children'),
               Output(component_id='plot2', component_property='children')],
              Input(component_id='demo-dropdown', component_property='value'))
# Place to define the callback function .
def display_selected_drive_charts(value):

    filtered_df = auto_data[auto_data['drive-wheels'] == value].groupby(
        ['drive-wheels', 'body-style'], as_index=False).mean()

    fig1 = px.pie(filtered_df, values='price',
                  names='body-style', title="Pie Chart")
    fig2 = px.bar(filtered_df, x='body-style', y='price', title='Bar Chart')

    return [dcc.Graph(figure=fig1),
            dcc.Graph(figure=fig2)]


# Run Application
if __name__ == '__main__':
    app.run_server()
