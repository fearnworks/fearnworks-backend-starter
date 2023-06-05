from dash import html, dcc, dash_table
from .page_utils import PageUtils
import pandas as pd
import plotly.graph_objects as go
import lorem

class GlobalMarketPage:
    """
    A class representing a GlobalMarket page for a report.
    """

    def __init__(self, color, globalMarket: pd.DataFrame, oecdCommercial):
        """
        Initializes a new instance of the GlobalMarketPage class.

        Args:
            color (str): The color scheme to use for the page. 
            globalMarket (pd.DataFrame): A pandas data frame containing the global market data.
            oecdCommercial (pd.DataFrame): A pandas data frame containing the OECD commercial data.

        """
        self.utils = PageUtils()
        self.color = color
        self.layout = self.create_global_market_page(globalMarket, oecdCommercial)
   

    def create_global_market_page(self, globalMarket: pd.DataFrame, oecdCommercial) -> html.Div:
        """
        Creates the layout for page 5 of the report.

        Args:
            app (dash.Dash): The Dash app instance.
            globalMarket (pd.DataFrame): A pandas data frame containing the global market data.
            oecdCommercial (pd.DataFrame): A pandas data frame containing the OECD commercial data.

        Returns:
            html.Div: The layout for page 5 of the report.

        Description:
            This method creates a layout for page 5 of the report. The layout contains several plots that visualize the global market and OECD commercial data. The types of plots used in this layout include line plots, scatter plots, and bar plots. The inputs to the plots include the global market and OECD commercial data frames, which are passed as arguments to the method. Common patterns used in this layout include using the same color scheme for related plots and using descriptive axis labels to make the plots easier to understand.
        """ 
        return html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.H6("Global Market"),
                                            html.Div(
                                                [html.P(lorem.paragraph())],
                                                className="page-5a",
                                            ),
                                            html.Div(
                                                [html.P(lorem.paragraph())],
                                                className="page-5b",
                                            ),
                                        ],
                                        className="page-5c",
                                    )
                                ],
                                className="eleven columns row",
                            ),
                            html.Div(
                                [html.P(lorem.paragraph(), className="page-5f")],
                                className="twelve columns row",
                            ),
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.Strong(
                                                        "Ultricies fusce vel, ad ultricies enim, at, egestas",
                                                        className="page-3h",
                                                    ),
                                                    html.P(
                                                        "Quis mauris dolor amet cubilia mattis, finibus magnis lacus",
                                                        className="page-3k",
                                                    ),
                                                ],
                                                className="title six columns",
                                            ),
                                            html.Div(
                                                [
                                                    html.Strong(
                                                        "Feugiat justo, aliquam feugiat justo suspendisse leo blandit",
                                                        className="page-3h",
                                                    ),
                                                    html.P(
                                                        "Praesent, morbi, rhoncus habitant at maximus mauris",
                                                        className="page-3k",
                                                    ),
                                                ],
                                                className="title six columns",
                                            ),
                                        ],
                                        className="thirdPage first row",
                                    )
                                ],
                                className="page-5g",
                            ),
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            dcc.Graph(
                                                figure={
                                                    "data": [
                                                        go.Bar(
                                                            x=globalMarket["x"],
                                                            y=globalMarket["y"],
                                                            marker={"color": self.color.color_1},
                                                            name="Global market imbalance",
                                                        )
                                                    ],
                                                    "layout": go.Layout(
                                                        autosize=True,
                                                        bargap=0.63,
                                                        dragmode="pan",
                                                        height=250,
                                                        width=320,
                                                        hovermode="closest",
                                                        legend={
                                                            "x": 0.0006061953460797935,
                                                            "y": -0.31665440684852813,
                                                            "bgcolor": "rgb(255, 255, 255, 0)",
                                                            "borderwidth": 0,
                                                            "font": {"size": 9},
                                                            "orientation": "h",
                                                        },
                                                        margin={
                                                            "r": 40,
                                                            "t": 5,
                                                            "b": 10,
                                                            "l": 20,
                                                            "pad": 0,
                                                        },
                                                        showlegend=True,
                                                        title="Click to enter Plot title",
                                                        xaxis={
                                                            "autorange": False,
                                                            "nticks": 18,
                                                            "range": [-0.5, 15.5],
                                                            "showgrid": False,
                                                            "tickfont": {"size": 9},
                                                            "tickmode": "linear",
                                                            "ticks": "",
                                                            "title": "Click to enter X axis title",
                                                            "type": "category",
                                                        },
                                                        yaxis={
                                                            "autorange": True,
                                                            "linecolor": "rgb(176, 177, 178)",
                                                            "nticks": 10,
                                                            "range": [
                                                                -1283.8982436029166,
                                                                3012.5614936594166,
                                                            ],
                                                            "showgrid": False,
                                                            "showline": True,
                                                            "tickfont": {"size": 9},
                                                            "ticks": "outside",
                                                            "title": "",
                                                            "type": "linear",
                                                            "zeroline": True,
                                                            "zerolinecolor": "rgb(176, 177, 178)",
                                                        },
                                                    ),
                                                }
                                            )
                                        ],
                                        className="six columns",
                                    ),
                                    html.Div(
                                        [
                                            dcc.Graph(
                                                figure={
                                                    "data": [
                                                        go.Scatter(
                                                            x=oecdCommercial[
                                                                "OECD commercial ex. US NGL & other, x"
                                                            ],
                                                            y=oecdCommercial[
                                                                "OECD commercial ex. US NGL & other, y"
                                                            ],
                                                            line={"color": self.color.color_1},
                                                            mode="lines",
                                                            name="OECD commercial ex. US NGL & other",
                                                        ),
                                                        go.Scatter(
                                                            x=oecdCommercial[
                                                                "Seasonal (2000-2014), x"
                                                            ],
                                                            y=oecdCommercial[
                                                                "Seasonal (2000-2014), y"
                                                            ],
                                                            line={"color": self.color.color_2},
                                                            mode="lines",
                                                            name="Seasonal (2000-2014)",
                                                        ),
                                                    ],
                                                    "layout": go.Layout(
                                                        autosize=True,
                                                        bargap=0.63,
                                                        dragmode="pan",
                                                        height=250,
                                                        width=320,
                                                        hovermode="closest",
                                                        legend={
                                                            "x": 0.0006061953460797935,
                                                            "y": -0.31665440684852813,
                                                            "bgcolor": "rgb(255, 255, 255, 0)",
                                                            "borderwidth": 0,
                                                            "font": {"size": 9},
                                                            "orientation": "h",
                                                        },
                                                        margin={
                                                            "r": 40,
                                                            "t": 5,
                                                            "b": 10,
                                                            "l": 40,
                                                            "pad": 0,
                                                        },
                                                        showlegend=True,
                                                        title="Click to enter Plot title",
                                                        xaxis={
                                                            "autorange": False,
                                                            "linecolor": "rgb(190, 191, 192)",
                                                            "nticks": 17,
                                                            "range": [-0.5, 16],
                                                            "showgrid": False,
                                                            "showline": False,
                                                            "tickfont": {"size": 9},
                                                            "ticks": "",
                                                            "ticksuffix": " ",
                                                            "title": "",
                                                            "type": "category",
                                                            "zeroline": False,
                                                            "zerolinecolor": "rgb(190, 191, 192)",
                                                        },
                                                        yaxis={
                                                            "autorange": False,
                                                            "linecolor": "rgb(190, 191, 192)",
                                                            "nticks": 10,
                                                            "range": [-800, 1000],
                                                            "showgrid": False,
                                                            "showline": True,
                                                            "tickfont": {"size": 10},
                                                            "ticks": "outside",
                                                            "ticksuffix": " ",
                                                            "title": "",
                                                            "type": "linear",
                                                            "zeroline": True,
                                                            "zerolinecolor": "rgb(190, 191, 192)",
                                                        },
                                                    ),
                                                }
                                            )
                                        ],
                                        className="six columns",
                                    ),
                                ],
                                className="page-1i",
                            ),
                        ],
                        className="subpage",
                    )
                ],
                className="page",
            )
   