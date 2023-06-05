from dash import html, dcc, dash_table
from .page_utils import PageUtils
import pandas as pd
import plotly.graph_objects as go
import lorem

class BondAnalysisPage:
    """
    A class representing a bond analysis page for a report.
    """

    def __init__(self, color, epxEquity: pd.DataFrame):
        """
        Initializes a new instance of the ForecastPage class.

        Args:
            color (str): The color scheme to use for the page. 
            epxEquity (pd.DataFrame): A DataFrame containing epxEquity data.
        """
        self.utils = PageUtils()
        self.color = color
        self.layout = self.create_bond_analysis(epxEquity)

    def create_bond_analysis(self, epxEquity) -> html.Div:
        """
        Creates a Dash layout for the bond analysis page.

        
        """
        return html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.P(
                                            lorem.paragraph() * 3, className="page-7a"
                                        ),
                                        html.P(
                                            lorem.paragraph() * 2, className="page-7a"
                                        ),
                                        html.P(lorem.paragraph(), className="page-7a"),
                                        html.P(lorem.paragraph(), className="page-7a"),
                                    ],
                                    className="page-7b",
                                )
                            ],
                            className="six columns",
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.Strong(
                                                    "Pg 7  elementum congue penatibus massa, eu sed sed dolor",
                                                    className="page-3h",
                                                ),
                                                html.Div(
                                                    [
                                                        dcc.Graph(
                                                            figure={
                                                                "data": [
                                                                    go.Bar(
                                                                        x=[
                                                                            "AAA",
                                                                            "AA",
                                                                            "A",
                                                                            "BBB",
                                                                            "BB",
                                                                            "B",
                                                                            "CCC",
                                                                        ],
                                                                        y=[
                                                                            "1497",
                                                                            "976",
                                                                            "1016",
                                                                            "1739",
                                                                            "993",
                                                                            "545",
                                                                            "31",
                                                                        ],
                                                                        marker={
                                                                            "color": self.color.color_1
                                                                        },
                                                                        name="y",
                                                                    )
                                                                ],
                                                                "layout": go.Layout(
                                                                    height=300,
                                                                    hovermode="closest",
                                                                    autosize=True,
                                                                    bargap=0.75,
                                                                    legend={
                                                                        "x": 0.16039179104479998,
                                                                        "y": -0.2720578174979476,
                                                                        "bgcolor": "rgb(255, 255, 255, 0)",
                                                                        "bordercolor": "rgba(68, 68, 68, 0)",
                                                                        "font": {
                                                                            "color": "rgb(68, 68, 68)",
                                                                            "size": 10,
                                                                        },
                                                                        "orientation": "h",
                                                                        "traceorder": "normal",
                                                                    },
                                                                    margin={
                                                                        "r": 0,
                                                                        "t": 10,
                                                                        "b": 30,
                                                                        "l": 60,
                                                                    },
                                                                    xaxis={
                                                                        "autorange": False,
                                                                        "nticks": 10,
                                                                        "range": [
                                                                            -0.5,
                                                                            6.5,
                                                                        ],
                                                                        "tickfont": {
                                                                            "size": 9
                                                                        },
                                                                        "ticks": "",
                                                                        "title": "",
                                                                        "type": "category",
                                                                    },
                                                                    yaxis={
                                                                        "autorange": False,
                                                                        "dtick": 250,
                                                                        "nticks": 9,
                                                                        "range": [
                                                                            0,
                                                                            2250,
                                                                        ],
                                                                        "showgrid": False,
                                                                        "showline": True,
                                                                        "tickfont": {
                                                                            "size": 9
                                                                        },
                                                                        "ticks": "outside",
                                                                        "ticksuffix": " ",
                                                                        "title": "2015E production by rating (mboe)<br><br>",
                                                                        "titlefont": {
                                                                            "size": 9
                                                                        },
                                                                        "type": "linear",
                                                                        "zeroline": True,
                                                                    },
                                                                ),
                                                            }
                                                        )
                                                    ]
                                                ),
                                            ],
                                            className="page-7c",
                                        ),
                                        html.Div(
                                            [
                                                html.Strong(
                                                    "At velit pharetra ac fusce sit dictum pellentesque, dictumst",
                                                    className="page-3h",
                                                ),
                                                html.Div(
                                                    dcc.Graph(
                                                        figure={
                                                            "data": [
                                                                go.Scatter(
                                                                    x=epxEquity[
                                                                        "EPX equity sector, x"
                                                                    ],
                                                                    y=epxEquity[
                                                                        "EPX equity sector, y"
                                                                    ],
                                                                    line={
                                                                        "color": self.color.color_1,
                                                                        "width": 2,
                                                                    },
                                                                    mode="lines",
                                                                    name="EPX equity sector",
                                                                    visible=True,
                                                                ),
                                                                go.Scatter(
                                                                    x=epxEquity[
                                                                        "WTI 2-yr swap, x"
                                                                    ],
                                                                    y=epxEquity[
                                                                        "WTI 2-yr swap, y"
                                                                    ],
                                                                    line={
                                                                        "color": self.color.color_2,
                                                                        "width": 2,
                                                                    },
                                                                    mode="lines",
                                                                    name="WTI 2-yr swap",
                                                                    visible=True,
                                                                ),
                                                                go.Scatter(
                                                                    x=epxEquity[
                                                                        "HY energy spread ratio (rhs, inverted), x"
                                                                    ],
                                                                    y=epxEquity[
                                                                        "HY energy spread ratio (rhs, inverted), y"
                                                                    ],
                                                                    line={
                                                                        "color": "red",
                                                                        "width": 2,
                                                                    },
                                                                    mode="lines",
                                                                    name="HY energy spread ratio (rhs, inverted)",
                                                                    visible=True,
                                                                ),
                                                            ],
                                                            "layout": go.Layout(
                                                                height=300,
                                                                autosize=True,
                                                                hovermode="closest",
                                                                legend={
                                                                    "x": 0.008033242860512229,
                                                                    "y": -0.3007047167087806,
                                                                    "bgcolor": "rgba(255, 255, 255, 0)",
                                                                    "font": {
                                                                        "color": "rgb(68, 68, 68)",
                                                                        "size": 9,
                                                                    },
                                                                    "orientation": "h",
                                                                },
                                                                margin={
                                                                    "r": 30,
                                                                    "t": 10,
                                                                    "b": 20,
                                                                    "l": 30,
                                                                },
                                                                showlegend=True,
                                                                xaxis={
                                                                    "autorange": False,
                                                                    "linecolor": "rgb(130, 132, 134)",
                                                                    "linewidth": 1,
                                                                    "nticks": 14,
                                                                    "range": [0, 12],
                                                                    "showgrid": False,
                                                                    "showline": True,
                                                                    "tickfont": {
                                                                        "color": "rgb(68, 68, 68)",
                                                                        "size": 9,
                                                                    },
                                                                    "ticks": "outside",
                                                                    "ticktext": [
                                                                        "Sep-14",
                                                                        "Oct-14",
                                                                        "Nov-14",
                                                                        "Dec-14",
                                                                        "Jan-15",
                                                                        "Feb-15",
                                                                        "Mar-15",
                                                                        "Apr-15",
                                                                        "May-15",
                                                                        "Jun-15",
                                                                        "July-15",
                                                                        "Aug-15",
                                                                    ],
                                                                    "tickvals": [
                                                                        0,
                                                                        1,
                                                                        2,
                                                                        3,
                                                                        4,
                                                                        5,
                                                                        6,
                                                                        7,
                                                                        8,
                                                                        9,
                                                                        10,
                                                                        11,
                                                                    ],
                                                                    "title": "",
                                                                    "type": "linear",
                                                                    "zeroline": False,
                                                                },
                                                                yaxis={
                                                                    "autorange": False,
                                                                    "linecolor": "rgb(130, 132, 134)",
                                                                    "nticks": 8,
                                                                    "range": [30, 100],
                                                                    "showgrid": False,
                                                                    "showline": True,
                                                                    "tickfont": {
                                                                        "size": 9
                                                                    },
                                                                    "ticks": "outside",
                                                                    "title": "",
                                                                    "type": "linear",
                                                                    "zeroline": True,
                                                                },
                                                                yaxis2={
                                                                    "anchor": "x",
                                                                    "linecolor": "rgb(130, 132, 134)",
                                                                    "nticks": 10,
                                                                    "overlaying": "y",
                                                                    "range": [1.8, 0.9],
                                                                    "showgrid": False,
                                                                    "showline": True,
                                                                    "side": "right",
                                                                    "tickfont": {
                                                                        "size": 9
                                                                    },
                                                                    "ticks": "outside",
                                                                    "title": "Click to enter Y axis title",
                                                                    "type": "linear",
                                                                    "zeroline": False,
                                                                },
                                                            ),
                                                        }
                                                    )
                                                ),
                                            ],
                                            className="page-1i",
                                        ),
                                    ],
                                    className="twelve columns",
                                )
                            ],
                            className="page-7d",
                        ),
                    ],
                    className="subpage",
                )
            ],
            className="page",
        )
    