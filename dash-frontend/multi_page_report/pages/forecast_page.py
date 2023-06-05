from dash import html, dcc, dash_table
from .page_utils import PageUtils
import pandas as pd
import plotly.graph_objects as go
import lorem

class ForecastPage:
    """
    A class representing a forecast page for a report.
    """

    def __init__(self, color, app,  wtiPrices: pd.DataFrame):
        """
        Initializes a new instance of the ForecastPage class.

        Args:
            color (str): The color scheme to use for the page. 
            wtiPrices (pd.DataFrame): A DataFrame containing WTI prices and forecasts.
        """
        self.utils = PageUtils()
        self.color = color
        self.layout = self.create_forecast_page(app, wtiPrices)
   
    def create_forecast_page(self, app, wtiPrices: pd.DataFrame) -> html.Div:
         # Page 6
        return html.Div(
            [
                html.Div(
                    [
                        html.Div([html.P(lorem.paragraph() * 3)], className="page-6"),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.Strong(
                                                    "Pg 6 velit pharetra ac fusce sit dictum pellentesque",
                                                    className="eleven columns",
                                                )
                                            ],
                                            className="page-3h",
                                        ),
                                        html.Div(
                                            [
                                                dcc.Graph(
                                                    figure={
                                                        "data": [
                                                            go.Scatter(
                                                                x=wtiPrices[
                                                                    "WTI Prices, x"
                                                                ],
                                                                y=wtiPrices[
                                                                    "WTI Prices, y"
                                                                ],
                                                                line={
                                                                    "color": self.color.color_1,
                                                                    "dash": "solid",
                                                                },
                                                                mode="lines",
                                                                name="WTI Prices",
                                                            ),
                                                            go.Scatter(
                                                                x=wtiPrices[
                                                                    "Sep-15 forecast, x"
                                                                ],
                                                                y=wtiPrices[
                                                                    "Sep-15 forecast, y"
                                                                ],
                                                                line={
                                                                    "color": "rgb(228, 31, 35)"
                                                                },
                                                                mode="lines",
                                                                name="Sep-15 forecast",
                                                            ),
                                                            go.Scatter(
                                                                x=wtiPrices[
                                                                    "Forward, x"
                                                                ],
                                                                y=wtiPrices[
                                                                    "Forward, y"
                                                                ],
                                                                line={
                                                                    "color": self.color.color_2,
                                                                    "dash": "solid",
                                                                },
                                                                mode="lines",
                                                                name="Forward",
                                                            ),
                                                            go.Scatter(
                                                                x=wtiPrices[
                                                                    "May-15 forecast, x"
                                                                ],
                                                                y=wtiPrices[
                                                                    "May-15 forecast, y"
                                                                ],
                                                                line={
                                                                    "color": self.color.color_3,
                                                                    "dash": "solid",
                                                                },
                                                                mode="lines",
                                                                name="Forward",
                                                            ),
                                                        ],
                                                        "layout": go.Layout(
                                                            height=250,
                                                            hovermode="closest",
                                                            legend={
                                                                "x": 0.16039179104479998,
                                                                "y": 1,
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
                                                                "r": 40,
                                                                "t": 5,
                                                                "b": 30,
                                                                "l": 40,
                                                            },
                                                            showlegend=True,
                                                            xaxis={
                                                                "autorange": False,
                                                                "linecolor": "rgb(130, 132, 134)",
                                                                "mirror": False,
                                                                "nticks": 14,
                                                                "range": [0, 14],
                                                                "showgrid": False,
                                                                "showline": True,
                                                                "tickfont": {
                                                                    "color": "rgb(68, 68, 68)",
                                                                    "size": 9,
                                                                },
                                                                "ticks": "outside",
                                                                "ticktext": [
                                                                    "Sep-14",
                                                                    "Nov-14",
                                                                    "Jan-15",
                                                                    "Mar-15",
                                                                    "May-15",
                                                                    "Jul-15",
                                                                    "Sep-15",
                                                                    "Nov-15",
                                                                    "Jan-16",
                                                                    "Mar-16",
                                                                    "May-16",
                                                                    "Jul-16",
                                                                    "Sept-16",
                                                                    "Nov-16",
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
                                                                    12,
                                                                    13,
                                                                ],
                                                                "title": "",
                                                                "type": "linear",
                                                                "zeroline": False,
                                                                "zerolinecolor": "rgb(130, 132, 134)",
                                                            },
                                                            yaxis={
                                                                "autorange": False,
                                                                "linecolor": "rgb(130, 132, 134)",
                                                                "nticks": 8,
                                                                "range": [30, 100],
                                                                "showline": True,
                                                                "tickfont": {
                                                                    "color": "rgb(68, 68, 68)",
                                                                    "size": 10,
                                                                },
                                                                "ticks": "outside",
                                                                "ticksuffix": " ",
                                                                "title": "",
                                                                "type": "linear",
                                                                "zeroline": True,
                                                                "zerolinecolor": "rgb(130, 132, 134)",
                                                            },
                                                        ),
                                                    }
                                                )
                                            ]
                                        ),
                                    ],
                                    className="eleven columns",
                                )
                            ],
                            className="page-2c",
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.Div(
                                                    [
                                                        html.Strong(
                                                            "At velit pharetra ac fusce sit dictum pellentesque",
                                                            className="page-3h",
                                                        ),
                                                        html.P(
                                                            lorem.paragraph() * 3,
                                                            className="page-2c",
                                                        ),
                                                    ],
                                                    className="page-6a",
                                                )
                                            ],
                                            className="five columns",
                                        ),
                                        html.Div(
                                            [
                                                html.Div(
                                                    [
                                                        html.Strong(
                                                            "Vehicula elementum congue penatibus massa, eu sed",
                                                            className="page-6d",
                                                        ),
                                                        html.Div(
                                                            html.Img(
                                                                src=app.get_asset_url(
                                                                    "DBkxRT2.png"
                                                                ),
                                                                className="page-6b",
                                                            )
                                                        ),
                                                    ],
                                                    className="page-6c",
                                                )
                                            ],
                                            className="six columns",
                                        ),
                                    ],
                                    className="thirdPage row",
                                )
                            ],
                            className="page-6e",
                        ),
                    ],
                    className="subpage",
                )
            ],
            className="page",
        )
    