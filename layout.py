import dash
from dash import html, dcc, Input, Output, callback, clientside_callback, State, Dash, ctx
import dash_bootstrap_components as dbc
import pandas as pd
from dash_svg import Svg, G, Path
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from utils import get_avg_value, get_difference, load_data
# define the main topic
topic = "Connectivity"


try:
    with open("config.json", 'r', encoding='utf-8') as file:
        config = json.load(file)
except Exception as e:
    print(f"An error occurred: {e}")
df = load_data()
tooltips = config[topic]["tooltips"]
button_dict1 = config[topic]["button_dict1"]
button_dict2 = config[topic]["button_dict2"]
featured_indicators = config[topic]["featured-indicators"]

year_values = [2017, 2018, 2019, 2020]


app = Dash(__name__)

server = app.server

app.layout =     html.Section(
        children=[
            html.Div(
                className="section main-chart",
                children=[
                    html.Div(
                        className="main-chart-comments",
                        children=[
                            html.Div(className="main-comments-section",
                                     children=[
                                         html.Div(
                                             className="main-title", children=[
                                                 html.H2(
                                                     className="title",
                                                     children=button_dict1["main-title"])
                                             ]
                                         ),
                                         html.Div(
                                             className="main-title-description",
                                             children=[
                                                 html.P(
                                                     className="description",
                                                     children=[
                                                         "Lorem ipsum dolor, sit amet consectetur adipisicing elit. A expedita, ea possimus laboriosam aut et nisi facilis excepturi placeat, quis voluptatem dolorum. Laboriosam natus porro dolore facilis laborum a esse."
                                                     ]
                                                 )
                                             ]
                                         ),
                                         #   Main statistics section
                                         html.Div(
                                             className="main-stats-section",
                                             children=[
                                                 html.H3(
                                                     className="stats-title",
                                                     children=[
                                                         "Numbers based on selection"]
                                                 ),
                                                 html.Div(
                                                     className="stats-main toggle-stat",
                                                     children=[
                                                         html.P(
                                                             className="value color0",
                                                             children=[
                                                                 html.Span(
                                                                     id="summary-line-{}".format(
                                                                         button_dict1["btn-title"]),
                                                                     className="value-number"
                                                                 ),
                                                                 html.Span(
                                                                     id="summary-line-suffix-{}".format(
                                                                         button_dict1["btn-title"]),
                                                                     className="value-suffix"
                                                                 )
                                                             ]
                                                         ),
                                                         html.P(
                                                             button_dict1["sum-value-description"][0],
                                                             className="description"
                                                         )
                                                     ]
                                                 ),
                                                 html.Div(
                                                     className="stats-content",
                                                     children=[
                                                         html.Div(
                                                             id="stats-first-{}".format(
                                                                 button_dict1["btn-title"]),
                                                             className="mini-stats-container toggle-stat",
                                                             children=[
                                                                 html.Div(
                                                                     className="stats-position two-values",
                                                                     children=[
                                                                         html.P(
                                                                             className="value color1",
                                                                             children=[
                                                                                 html.Span(
                                                                                     id="first-val-line-{}".format(button_dict1["btn-title"]), className="value-number"),
                                                                                 html.Span(
                                                                                     id="first-val-line-suffix-{}".format(button_dict1["btn-title"]), className="value-suffix")
                                                                             ]
                                                                         ),
                                                                         html.Div(
                                                                             className="description",
                                                                             children=html.Span(
                                                                                 "Percent of {}".format(button_dict1["sum-value-description"][1]))
                                                                         )
                                                                     ]
                                                                 ),
                                                                 html.Div(
                                                                     className="stats-position two-values",
                                                                     children=[
                                                                         html.P(
                                                                             className="value color1",
                                                                             children=[
                                                                                 html.Span(
                                                                                     id="first-percent-line-{}".format(button_dict1["btn-title"]), className="value-number"),
                                                                                 html.Span(
                                                                                     id="precent-suffix1-{}".format(button_dict1["btn-title"]), className="value-suffix")
                                                                             ]
                                                                         ),
                                                                         html.Div(
                                                                             className="description",
                                                                             children=html.Span(
                                                                                 "Percentage change over the past year")
                                                                         )
                                                                     ]
                                                                 ),
                                                             ]),
                                                         html.Div(
                                                             className="mini-stats-container toggle-stat",
                                                             children=[
                                                                 html.Div(
                                                                     className="stats-position two-values",
                                                                     children=[
                                                                         html.P(
                                                                             className="value color2",
                                                                             children=[
                                                                                 html.Span(
                                                                                     id="second-val-line-{}".format(button_dict1["btn-title"]), className="value-number"),
                                                                                 html.Span(
                                                                                     id="second-val-line-suffix-{}".format(button_dict1["btn-title"]), className="value-suffix")
                                                                             ]
                                                                         ),
                                                                         html.Div(
                                                                             className="description",
                                                                             children=html.Span(
                                                                                 "Percent of {}".format(button_dict1["sum-value-description"][2]))
                                                                         )
                                                                     ]
                                                                 ),
                                                                 html.Div(
                                                                     className="stats-position two-values",
                                                                     children=[
                                                                         html.P(
                                                                             className="value color2",
                                                                             children=[
                                                                                 html.Span(
                                                                                     id="second-percent-line-{}".format(button_dict1["btn-title"]), className="value-number"),
                                                                                 html.Span(
                                                                                     id="precent-suffix2-{}".format(button_dict1["btn-title"]), className="value-suffix")
                                                                             ]
                                                                         ),
                                                                         html.Div(
                                                                             className="description",
                                                                             children=html.Span(
                                                                                 "Percentage change over the past year")
                                                                         )
                                                                     ]
                                                                 ),
                                                             ]
                                                         )

                                                     ]
                                                 )
                                             ]
                                         )
                                     ])
                        ]),
                    html.Div(
                        className="main-chart-main",
                        children=[
                            dcc.Graph(
                                id="first-chart-{}".format(
                                    button_dict1["btn-title"]),
                                config={'displayModeBar': False, 'showAxisDragHandles': False}),
                            html.Div(className="year-btn-wrapper", children=[
                                html.Div(
                                    "{}".format(year_values[i]),
                                    id="y-{}-{}".format(
                                        year_values[i], button_dict1["btn-title"]),
                                    className="year-btn {}".format(
                                        "active" if i == len(year_values)-1 else ""),
                                ) for i in range(0, len(year_values))
                            ]),
                        ]),
                    html.Div(
                        className="side-menu",
                        children=[
                            html.Aside(
                                className="filters",
                                children=[
                                    html.Span("{}".format(
                                        button_dict1["second-toggle-title"])),
                                    html.Div(
                                        className="filter-selection",
                                        children=[
                                            html.Ul(
                                                children=[
                                                    html.Li(
                                                        className="dots-buttons",
                                                        id="{}-{}".format(i,
                                                                          idx),
                                                        children=[
                                                            html.Span(
                                                                className="filter-dot active"),
                                                            html.Span(
                                                                "{}".format(button_dict1["sum-value-description"][idx]), className="filter-text active"),
                                                        ],
                                                        n_clicks=0,
                                                    ) for idx, i in enumerate(button_dict1["sum-values"])
                                                ]

                                            )

                                        ]
                                    ),
                                    html.Div(className="arrow-left"),

                                ],
                            ),
                            html.Div(className="download-option", children=[
                                html.Button("Download Report",
                                            className="download-button"),
                                dcc.Store(id=f"{topic}-df-store"),
                                dcc.Store(id=f"{topic}-df-store-2"),
                                dcc.Store(id=f"{topic}-year-store"),
                                dcc.Store(id=f"{topic}-year-store-2"),
                                html.Div(id=f"callback1-{topic}"),
                                html.Div(id=f"callback2-{topic}"),
                            ])
                        ]
                    ),
                ],

            )],

        className="section",
        id="section2",
        **{"data-label": "About Us"}
    )

@callback(
    Output(f"{topic}-year-store", "data"),
    [Input("y-{}-{}".format(year, button_dict1["btn-title"]), "n_clicks")
     for year in year_values]
)
def update_vertical_line(*args):
    button_id = ctx.triggered_id
    pos_x = df["Year"].max()  # Initialize pos_x to a default value

    if button_id is not None:
        for i in range(0, int(len(args))):
            if button_id == "y-{}-{}".format(year_values[i], button_dict1["btn-title"]):
                pos_x = year_values[i]
                break  # Exit the loop once a match is found
    return pos_x
@callback(
    Output("first-chart-{}".format(button_dict1["btn-title"]), "figure"),
    #
    [Output("{}-{}".format(i, idx), "n_clicks")
     for idx, i in enumerate(button_dict1["sum-values"])],
    Output(f"{topic}-df-store", "data"),
    [Input("{}-{}".format(i, idx), "n_clicks")
     for idx, i in enumerate(button_dict1["sum-values"])],
    Input(f"{topic}-year-store", "data"),
)
def update_line_chart(dot1, dot2, dot3, pos_x):
    # Filter the DataFrame based on the state of each dot
    indicators_to_include = button_dict1["indicator-name"]
    filtered_df = df.loc[df['Indicator Name'].isin(indicators_to_include)]
    average_values = filtered_df.groupby(['Indicator Name', 'Year'])[
        'Indicator Value'].mean().reset_index()
    plot_data = average_values
    sum_average_values = average_values.groupby(
        'Year')['Indicator Value'].sum().reset_index()
    sum_average_values['Indicator Name'] = 'Sum of Average Values'
    plot_data = pd.concat([average_values, sum_average_values])
    # serialize data to store it in dcc.Store
    serialized_df = plot_data.to_json(date_format="iso", orient="split")
    if dot1 % 2 == 1:
        plot_data = plot_data[plot_data['Indicator Name']
                              != 'Sum of Average Values']
    if dot2 % 2 == 1:
        plot_data = plot_data[plot_data['Indicator Name'] !=
                              button_dict1["indicator-name"][0]]
    if dot3 % 2 == 1:
        plot_data = plot_data[plot_data['Indicator Name'] !=
                              button_dict1["indicator-name"][1]]

    fig = px.line(plot_data, x='Year', y='Indicator Value', color='Indicator Name',
                  line_shape='linear')
    # Make the lines thicker
    fig.update_traces(line=dict(width=3))
    # Update the colors for each indicator
    fig.update_traces(selector=dict(
        name='Sum of Average Values'), line=dict(color='#fffe7e'))
    fig.update_traces(selector=dict(
        name=button_dict1["indicator-name"][0]), line=dict(color='#1dcf53'))
    fig.update_traces(selector=dict(
        name=button_dict1["indicator-name"][1]), line=dict(color='#0060ff'))

    # Hide the legend
    fig.update_layout(showlegend=False)

    # Make the chart background transparent
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                      plot_bgcolor='rgba(0,0,0,0)')
    # Set the x-axis tickvals and ticktext to display only integer values
    fig.update_xaxes(tickvals=plot_data['Year'].unique(
    ), ticktext=plot_data['Year'].unique().astype(int))

    # hide the x-axis
    fig.update_xaxes(visible=False)

    # Shift the x-axis slightly to the right
    if len(plot_data) > 0:
        x_range = [min(plot_data['Year']) - 0.1, max(plot_data['Year']) + 0.1]
        fig.update_layout(xaxis_range=x_range)
    # Disable grid lines
    fig.update_xaxes(showgrid=False, title='')
    fig.update_yaxes(tickfont=dict(color='white'),
                     gridcolor='#0d1929', title='')

    fig.update_layout(font=dict(color='white'))
    # Remove the title
    fig.update_layout(title='')
    # get the latest clicked button
    button_id = ctx.triggered_id if not None else 'No clicks yet'

    fig.add_vline(
        x=pos_x, line_width=2, line_dash="dot",
        line_color="#d09c4f")
    # "{}-{}".format(i, idx) for idx, i in enumerate(button_dict1["sum-values"])

    if dot1 % 2 == 1 and dot2 % 2 == 1 and dot3 % 2 == 1:
        if "0" in button_id:
            return dash.no_update, 0, dot2, dot3, serialized_df
        if "1" in button_id:
            return dash.no_update, dot1, 0, dot3, serialized_df
        if "2" in button_id:
            return dash.no_update, dot1, dot2, 0, serialized_df
    else:
        return fig, dot1, dot2, dot3, serialized_df
# callback to make the line chart in the second seciton

@callback(
    Output("summary-line-{}".format(button_dict1["btn-title"]), "children"),
    Output(
        "summary-line-suffix-{}".format(button_dict1["btn-title"]), "children"),
    Output("first-val-line-{}".format(button_dict1["btn-title"]), "children"),
    Output(
        "first-val-line-suffix-{}".format(button_dict1["btn-title"]), "children"),
    Output(
        "first-percent-line-{}".format(button_dict1["btn-title"]), "children"),
    Output("precent-suffix1-{}".format(button_dict1["btn-title"]), "children"),
    Output("second-val-line-{}".format(button_dict1["btn-title"]), "children"),
    Output(
        "second-val-line-suffix-{}".format(button_dict1["btn-title"]), "children"),
    Output(
        "second-percent-line-{}".format(button_dict1["btn-title"]), "children"),
    Output("precent-suffix2-{}".format(button_dict1["btn-title"]), "children"),
    Input(f"{topic}-df-store", "data"),
    Input(f"{topic}-year-store", "data"),
)
def update_line_chart(jsonified_cleaned_data, selected_year):
    dff = pd.read_json(jsonified_cleaned_data, orient='split')
    dff_2 = dff[dff["Year"] == selected_year]
    if selected_year == dff["Year"].min():
        differences = ["-", "-", "-"]
        return round(dff_2.iloc[2, 2], 1), button_dict1["indicator-unit"], round(dff_2.iloc[1, 2], 1),\
            button_dict1["indicator-unit"], differences[1], "", round(dff_2.iloc[0, 2], 1), \
            button_dict1["indicator-unit"], differences[0], ""
    else:
        differences = get_difference(dff, selected_year)
        return round(dff_2.iloc[2, 2], 1), button_dict1["indicator-unit"], \
            round(dff_2.iloc[1, 2], 1), button_dict1["indicator-unit"], "{:.0f}".format(differences[1]), "%", \
            round(
                dff_2.iloc[0, 2], 1), button_dict1["indicator-unit"], "{:.0f}".format(differences[0]), "%"

clientside_callback(
    """
    function updateYearButtons() {
        const yearBtns = document.querySelectorAll('.year-btn');

        // Add a click event listener to each "year-btn"
        yearBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Remove the "active" class from all "year-btn" elements
                yearBtns.forEach(btn => {
                    btn.classList.remove('active');
                });

                // Add the "active" class to the clicked element
                btn.classList.add('active');
            });
        });
    }
    """,
    Output(f"callback1-{topic}", 'children'),
    Input(f"callback1-{topic}", 'children')
)
clientside_callback(
    """function (id) {
    newFunc();
    return window.dash_clientside.no_update
}""",
    Output(f"callback2-{topic}", 'children'), Input(f"callback2-{topic}", 'children'))

if __name__ == "__main__":
    app.run_server(port=8089, debug=True)