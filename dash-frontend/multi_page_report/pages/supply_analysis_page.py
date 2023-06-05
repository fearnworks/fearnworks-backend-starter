from dash import html, dcc, dash_table
from .page_utils import PageUtils
import pandas as pd
import plotly.graph_objects as go
import lorem

class SupplyReserveAnalysisPage:
    """
    A class representing a supply analysis page for a report.
    """

    def __init__(self, color, app, forSpr: pd.DataFrame):
        """
        Initializes a new instance of the GlobalMarketPage class.

        Args:
            color (str): The color to use for the page.
            app (Dash): The Dash app to use for the page.
            forSpr (pd.DataFrame): Petroleum Reserve data 
        """
        self.utils = PageUtils()
        self.color = color
        self.layout = self.create_supply_analysis_page(app, forSpr)
   

    def create_supply_analysis_page(self,app, forSpr: pd.DataFrame):
        # Page 9
        return html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.Div(
                                                    [
                                                        html.P(
                                                            "Pg 9 et libero nullam pretium quis est in sit. Commodo nec ante aenean a. Commodo at facilisis vestibulum cursus elementum nascetur et, placerat class aliquam convallis porttitor accumsan. Ultricies sed laoreet eleifend maximus venenatis",
                                                            className="page-3h",
                                                        ),
                                                        html.Strong(
                                                            "Congue nisl iaculis interdum cubilia maximus"
                                                        ),
                                                        html.Div(
                                                            [
                                                                html.Img(
                                                                    src=app.get_asset_url(
                                                                        "wX5mQYn.png"
                                                                    ),
                                                                    className="exhibit eleven columns",
                                                                )
                                                            ],
                                                            className="page-9a",
                                                        ),
                                                    ],
                                                    className="page-7a",
                                                ),
                                                html.Div(
                                                    [
                                                        html.P(
                                                            "Id nulla sollicitudin taciti ac tempus amet ligula accumsan. Elementum, nullam dui ligula ut. Adipiscing sed ultricies ut vitae augue etiam nostra nibh.",
                                                            className="page-3h",
                                                        ),
                                                        html.Strong(
                                                            "Convallis et eu habitant leo leo luctus venenatis"
                                                        ),
                                                        html.Div(
                                                            [
                                                                dcc.Graph(
                                                                    figure={
                                                                        "data": [
                                                                            go.Scatter(
                                                                                x=forSpr[
                                                                                    "OECD commercial ex. US NGL & other, x"
                                                                                ],
                                                                                y=forSpr[
                                                                                    "OECD commercial ex. US NGL & other, y"
                                                                                ],
                                                                                line={
                                                                                    "color": self.color.color_1,
                                                                                    "width": 2,
                                                                                },
                                                                                mode="lines",
                                                                                name="OECD commercial ex. US NGL & other",
                                                                                visible=True,
                                                                            ),
                                                                            go.Scatter(
                                                                                x=forSpr[
                                                                                    "Non-OECD stocks ex. for SPR, x"
                                                                                ],
                                                                                y=forSpr[
                                                                                    "Non-OECD stocks ex. for SPR, y"
                                                                                ],
                                                                                line={
                                                                                    "color": self.color.color_2,
                                                                                    "width": 2,
                                                                                },
                                                                                mode="lines",
                                                                                name="Non-OECD stocks ex. for SPR",
                                                                            ),
                                                                        ],
                                                                        "layout": go.Layout(
                                                                            annotations=[
                                                                                {
                                                                                    "x": 12.0815219907062,
                                                                                    "y": 948.201438849,
                                                                                    "font": {
                                                                                        "size": 9
                                                                                    },
                                                                                    "showarrow": False,
                                                                                    "text": "GS forecast",
                                                                                    "xref": "x",
                                                                                    "yref": "y",
                                                                                }
                                                                            ],
                                                                            height=300,
                                                                            autosize=True,
                                                                            dragmode="zoom",
                                                                            hovermode="closest",
                                                                            legend={
                                                                                "x": 0.0913178294574,
                                                                                "y": -0.167832167832,
                                                                                "bgcolor": "rgba(255, 255, 255, 0)",
                                                                                "font": {
                                                                                    "size": 9
                                                                                },
                                                                                "orientation": "h",
                                                                            },
                                                                            margin={
                                                                                "r": 10,
                                                                                "t": 10,
                                                                                "b": 0,
                                                                                "l": 40,
                                                                                "pad": 0,
                                                                            },
                                                                            shapes=[
                                                                                {
                                                                                    "line": {
                                                                                        "color": "rgb(68, 68, 68)",
                                                                                        "dash": "dot",
                                                                                        "width": 1,
                                                                                    },
                                                                                    "type": "line",
                                                                                    "x0": 0.6541331802525385,
                                                                                    "x1": 0.6541331802525385,
                                                                                    "xref": "paper",
                                                                                    "y0": 0,
                                                                                    "y1": 1,
                                                                                    "yref": "paper",
                                                                                }
                                                                            ],
                                                                            showlegend=True,
                                                                            xaxis={
                                                                                "autorange": False,
                                                                                "nticks": 10,
                                                                                "range": [
                                                                                    -0.25,
                                                                                    15.5,
                                                                                ],
                                                                                "showgrid": False,
                                                                                "showline": False,
                                                                                "tickfont": {
                                                                                    "size": 9
                                                                                },
                                                                                "ticktext": [
                                                                                    "1Q13",
                                                                                    "2Q13",
                                                                                    "3Q13",
                                                                                    "4Q13",
                                                                                    "1Q14",
                                                                                    "2Q14",
                                                                                    "3Q14",
                                                                                    "4Q14",
                                                                                    "1Q15",
                                                                                    "2Q15",
                                                                                    "3Q15E",
                                                                                    "4Q15E",
                                                                                    "1Q16E",
                                                                                    "2Q16E",
                                                                                    "3Q16E",
                                                                                    "4Q16E",
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
                                                                                    14,
                                                                                    15,
                                                                                ],
                                                                                "title": "",
                                                                                "type": "linear",
                                                                                "zerolinecolor": "rgb(130, 132, 134)",
                                                                                "zeroline": False,
                                                                                "zerolinewidth": 1,
                                                                            },
                                                                            yaxis={
                                                                                "autorange": False,
                                                                                "nticks": 10,
                                                                                "range": [
                                                                                    -800,
                                                                                    1000,
                                                                                ],
                                                                                "showgrid": False,
                                                                                "showline": True,
                                                                                "tickfont": {
                                                                                    "color": "rgb(68, 68, 68)",
                                                                                    "size": 9,
                                                                                },
                                                                                "ticks": "outside",
                                                                                "title": "",
                                                                                "type": "linear",
                                                                                "zeroline": True,
                                                                            },
                                                                        ),
                                                                    }
                                                                )
                                                            ],
                                                            className="page-1i",
                                                        ),
                                                    ],
                                                    className="page-9b",
                                                ),
                                            ],
                                            className="page-9c",
                                        )
                                    ],
                                    className="exibit six columns",
                                ),
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.P(lorem.paragraph()),
                                                html.P(lorem.paragraph()),
                                                html.P(lorem.paragraph()),
                                                html.P(lorem.paragraph()),
                                            ],
                                            className="page-2b",
                                        )
                                    ],
                                    className="five columns",
                                ),
                            ],
                            className="page-9d",
                        )
                    ],
                    className="subpage",
                )
            ],
            className="page",
        )
    
