from dash import html, dcc, dash_table
from .page_utils import PageUtils
from ..scatter_graphs import create_producer_scatter_graph
import pandas as pd
import plotly.graph_objects as go
import lorem

class AnomalyAnalysisPage:
    """
    A class representing a graph and block quote page for a report.

    Attributes:
        utils (PageUtils): An instance of the PageUtils class.
        color (str): The color to use for the graph.
        layout (dict): The layout of the anomaly analysis page.

    """

    def __init__(self, color: str, oecdIndustry: pd.DataFrame, productionCost: float, production2015: float, wtiOilprices: pd.DataFrame) -> None:
        """
        Initializes a new instance of the AnomalyAnalysisPage class.

        Args:
            color (str): The color to use for the graph.
            oecdIndustry (pd.DataFrame): A pandas DataFrame containing industry data.
            productionCost (float): The production cost.
            production2015 (float): The production cost in 2015.
            wtiOilprices (pd.DataFrame): A pandas DataFrame containing WTI oil prices.

        Returns:
            None
        """
        self.utils = PageUtils()
        self.color = color
        self.layout = self.create_anomaly_analysis_page(oecdIndustry, productionCost, production2015, wtiOilprices)


    def create_anomaly_analysis_page(self, oecdIndustry: pd.DataFrame, productionCost, production2015, wtiOilprices):
            """
            Creates an anomaly analysis page based on the given data.

            Args:
                oecdIndustry (pd.DataFrame): A pandas DataFrame containing industry data.
                productionCost (float): The production cost.
                production2015 (float): The production cost in 2015.
                wtiOilprices (pd.DataFrame): A pandas DataFrame containing WTI oil prices.

            Returns:
                None
            """
            producer_scatter_graph = create_producer_scatter_graph(production2015, self.color)
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
                                                    html.H5("Anomoly Analysis"),
                                                    html.P(
                                                        "Nulla diam conubia nec lacus urna in ligula nec ut egestas sed",
                                                        className="page-3k",
                                                    ),
                                                    html.Div(
                                                        [
                                                            dcc.Graph(
                                                                figure={
                                                                    "data": [
                                                                        go.Scatter(
                                                                            x=oecdIndustry[
                                                                                "OECD industry stock changes , x"
                                                                            ],
                                                                            y=oecdIndustry[
                                                                                "OECD industry stock changes , y"
                                                                            ],
                                                                            line={
                                                                                "color": self.color.color_1
                                                                            },
                                                                            mode="lines",
                                                                            name="OECD industry stock changes ",
                                                                        ),
                                                                        go.Scatter(
                                                                            x=oecdIndustry[
                                                                                "IEA miscellaneous to balance (rhs), x"
                                                                            ],
                                                                            y=oecdIndustry[
                                                                                "IEA miscellaneous to balance (rhs), y"
                                                                            ],
                                                                            line={
                                                                                "color": self.color.color_2
                                                                            },
                                                                            mode="lines",
                                                                            name="IEA miscellaneous to balance (rhs)",
                                                                            yaxis="y2",
                                                                        ),
                                                                    ],
                                                                    "layout": go.Layout(
                                                                        height=250,
                                                                        autosize=True,
                                                                        hovermode="closest",
                                                                        legend={
                                                                            "x": 0.0913178294574,
                                                                            "y": -0.167832167832,
                                                                            "bgcolor": "rgba(255, 255, 255, 0)",
                                                                            "orientation": "h",
                                                                        },
                                                                        margin={
                                                                            "r": 30,
                                                                            "t": 10,
                                                                            "b": 0,
                                                                            "l": 30,
                                                                        },
                                                                        shapes=[
                                                                            {
                                                                                "fillcolor": "rgba(31, 119, 180, 0)",
                                                                                "line": {
                                                                                    "color": "rgb(255, 0, 0)",
                                                                                    "dash": "dash",
                                                                                    "width": 1,
                                                                                },
                                                                                "opacity": 1,
                                                                                "type": "rect",
                                                                                "x0": 1997.25,
                                                                                "x1": 1998.75,
                                                                                "xref": "x",
                                                                                "y0": -1713.7349397590363,
                                                                                "y1": 2391.5662650602408,
                                                                                "yref": "y",
                                                                            },
                                                                            {
                                                                                "fillcolor": "rgba(31, 119, 180, 0)",
                                                                                "layer": "above",
                                                                                "line": {
                                                                                    "color": "rgb(255, 0, 0)",
                                                                                    "dash": "dash",
                                                                                    "width": 1,
                                                                                },
                                                                                "opacity": 1,
                                                                                "type": "rect",
                                                                                "x0": 2013.25,
                                                                                "x1": 2014.75,
                                                                                "xref": "x",
                                                                                "y0": -1674.2105263157894,
                                                                                "y1": 2286.315789473684,
                                                                                "yref": "y",
                                                                            },
                                                                        ],
                                                                        showlegend=True,
                                                                        xaxis={
                                                                            "autorange": False,
                                                                            "nticks": 30,
                                                                            "range": [
                                                                                1986,
                                                                                2015,
                                                                            ],
                                                                            "showgrid": False,
                                                                            "showline": True,
                                                                            # 'tickangle': "auto",
                                                                            "tickfont": {
                                                                                "size": 8
                                                                            },
                                                                            "tickprefix": "1Q",
                                                                            "ticks": "outside",
                                                                            "type": "linear",
                                                                            "zeroline": True,
                                                                        },
                                                                        yaxis={
                                                                            "autorange": False,
                                                                            "nticks": 10,
                                                                            "range": [
                                                                                -2000,
                                                                                2500,
                                                                            ],
                                                                            "showgrid": False,
                                                                            "showline": True,
                                                                            "tickfont": {
                                                                                "size": 9
                                                                            },
                                                                            "ticks": "outside",
                                                                            "type": "linear",
                                                                        },
                                                                        yaxis2={
                                                                            "anchor": "x",
                                                                            "autorange": False,
                                                                            "nticks": 12,
                                                                            "overlaying": "y",
                                                                            "range": [
                                                                                -2500,
                                                                                2500,
                                                                            ],
                                                                            "showgrid": False,
                                                                            "showline": True,
                                                                            "side": "right",
                                                                            "tickfont": {
                                                                                "size": 8
                                                                            },
                                                                            "ticks": "outside",
                                                                            "type": "linear",
                                                                            "zeroline": False,
                                                                        },
                                                                    ),
                                                                }
                                                            )
                                                        ]
                                                    ),
                                                ],
                                                className="thirdPage first row",
                                                # style={"marginTop": "0px"},
                                            )
                                        ]  # className="page-9e"
                                    ),
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.Strong(
                                                        "Risus amet quam, eget, lacus, orci, dui facilisis dolor sodales arcu facilisi consectetur",
                                                        className="page-3h",
                                                    ),
                                                    html.P(
                                                        "Diam, maximus ultricies neque adipiscing tellus eros proin",
                                                        className="page-3k",
                                                    ),
                                                    html.Div(
                                                        [
                                                            dcc.Graph(
                                                                figure={
                                                                    "data": [
                                                                        go.Scatter(
                                                                            x=wtiOilprices[
                                                                                "x"
                                                                            ],
                                                                            y=wtiOilprices[
                                                                                "y"
                                                                            ],
                                                                            line={
                                                                                "color": self.color.color_1
                                                                            },
                                                                            mode="lines",
                                                                            name="WTI oil prices (S/bbl, 2015 $)    ",
                                                                        )
                                                                    ],
                                                                    "layout": go.Layout(
                                                                        height=250,
                                                                        autosize=True,
                                                                        hovermode="closest",
                                                                        legend={
                                                                            "x": 0.16818221960553428,
                                                                            "y": -0.30969810073003856,
                                                                            "bgcolor": "rgba(255, 255, 255, 0)",
                                                                        },
                                                                        margin={
                                                                            "r": 10,
                                                                            "t": 10,
                                                                            "b": 40,
                                                                            "l": 30,
                                                                        },
                                                                        shapes=[
                                                                            {
                                                                                "fillcolor": "rgba(31, 119, 180, 0)",
                                                                                "line": {
                                                                                    "color": "rgb(255, 0, 0)",
                                                                                    "dash": "dash",
                                                                                    "width": 1,
                                                                                },
                                                                                "opacity": 1,
                                                                                "type": "rect",
                                                                                "x0": 1985.6994029850746,
                                                                                "x1": 1987.4587313432835,
                                                                                "xref": "x",
                                                                                "y0": 10,
                                                                                "y1": 85,
                                                                                "yref": "y",
                                                                            },
                                                                            {
                                                                                "fillcolor": "rgba(31, 119, 180, 0)",
                                                                                "layer": "above",
                                                                                "line": {
                                                                                    "color": "rgb(255, 0, 0)",
                                                                                    "dash": "dash",
                                                                                    "width": 1,
                                                                                },
                                                                                "opacity": 1,
                                                                                "type": "rect",
                                                                                "x0": 1998.1650746268656,
                                                                                "x1": 1999.989328358209,
                                                                                "xref": "x",
                                                                                "y0": 5,
                                                                                "y1": 70,
                                                                                "yref": "y",
                                                                            },
                                                                        ],
                                                                        showlegend=True,
                                                                        xaxis={
                                                                            "autorange": False,
                                                                            "nticks": 24,
                                                                            "range": [
                                                                                1972,
                                                                                2015.5,
                                                                            ],
                                                                            "showgrid": False,
                                                                            "showline": True,
                                                                            "tickfont": {
                                                                                "size": 9
                                                                            },
                                                                            "ticks": "outside",
                                                                            "titlefont": {
                                                                                "color": "rgb(92, 53, 143)"
                                                                            },
                                                                            "type": "linear",
                                                                            "zeroline": False,
                                                                        },
                                                                        yaxis={
                                                                            "autorange": False,
                                                                            "nticks": 1,
                                                                            "range": [
                                                                                0,
                                                                                180,
                                                                            ],
                                                                            "showgrid": False,
                                                                            "showline": True,
                                                                            "tickfont": {
                                                                                "size": 9
                                                                            },
                                                                            "ticks": "outside",
                                                                            "type": "linear",
                                                                        },
                                                                    ),
                                                                }
                                                            )
                                                        ]
                                                    ),
                                                ],
                                                className="thirdPage first row",
                                            )
                                        ],
                                        className="page-2c",
                                    ),
                                ],
                                className="page-2b",
                            ),
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.Strong(
                                                        "Porttitor felis eget nibh quam duis et at a massa varius.",
                                                        className="page-3h",
                                                    ),
                                                    html.P(
                                                        "Risus amet quam, eget, lacus, orci, dui facilisis ",
                                                        className="page-3k",
                                                    ),
                                                    ### Scatter Graph 1 
                                                    html.Div(
                                                        [
                                                            dcc.Graph(
                                                                figure={
                                                                    "data": [
                                                                        go.Scatter(
                                                                            x=productionCost[
                                                                                "x"
                                                                            ],
                                                                            y=productionCost[
                                                                                "y"
                                                                            ],
                                                                            line={
                                                                                "color": self.color.color_1
                                                                            },
                                                                            mode="lines",
                                                                        )
                                                                    ],
                                                                    "layout": go.Layout(
                                                                        height=200,
                                                                        margin={
                                                                            "r": 20,
                                                                            "t": 10,
                                                                            "b": 50,
                                                                            "l": 40,
                                                                        },
                                                                        xaxis={
                                                                            "autorange": False,
                                                                            "exponentformat": "none",
                                                                            "linecolor": "rgb(171, 172, 173)",
                                                                            "nticks": 5,
                                                                            "range": [
                                                                                0,
                                                                                40000,
                                                                            ],
                                                                            "showgrid": False,
                                                                            "showline": True,
                                                                            "tickfont": {
                                                                                "size": 9
                                                                            },
                                                                            "ticks": "outside",
                                                                            "title": "Cumulative peak oil production (kb/d)",
                                                                            "titlefont": {
                                                                                "size": 9
                                                                            },
                                                                            "type": "linear",
                                                                            "zeroline": False,
                                                                        },
                                                                        yaxis={
                                                                            "autorange": False,
                                                                            "linecolor": "rgb(171, 172, 173)",
                                                                            "nticks": 10,
                                                                            "range": [
                                                                                0,
                                                                                45,
                                                                            ],
                                                                            "showgrid": False,
                                                                            "showline": True,
                                                                            "tickfont": {
                                                                                "size": 9
                                                                            },
                                                                            "ticks": "outside",
                                                                            "title": "Production cost (US$/bbl)",
                                                                            "titlefont": {
                                                                                "size": 9
                                                                            },
                                                                            "type": "linear",
                                                                            "zeroline": False,
                                                                        },
                                                                    ),
                                                                }
                                                            )
                                                        ]
                                                    ),
                                                ],
                                                className="six columns",
                                            ),
                                            producer_scatter_graph],
                                        className="thirdPage first row",
                                    )
                                ],
                                className="page-2c",
                            ),
                        ],
                        className="subpage",
                    )
                ],
                className="page",
            )
        