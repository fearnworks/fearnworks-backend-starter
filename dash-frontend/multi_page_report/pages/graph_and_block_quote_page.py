from dash import html, dcc, dash_table
from .page_utils import PageUtils
import pandas as pd
import plotly.graph_objects as go
import lorem

class GraphAndBlockQuotePage:
    """
    A class representing a graph and block quote page for a report.
    """

    def __init__(self, color, supplyDemand: pd.DataFrame, actualSeasonal, industrialProd: pd.DataFrame, growthGdp: pd.DataFrame):
        """
        Initializes a new instance of the GraphAndBlockQuotePage class.

        Args:
            supplyDemand (pd.DataFrame): The supply and demand data to use in the graph.
            actualSeasonal (pd.DataFrame): The actual seasonal data to use in the graph.
            industrialProd (pd.DataFrame): The industrial production data to use in the graph.
            growthGdp (pd.DataFrame): The GDP growth data to use in the graph.

        """
        self.utils = PageUtils()
        self.color = color
        self.layout = self.create_graph_and_block_quote_page(supplyDemand, actualSeasonal, industrialProd, growthGdp)

    def create_graph_and_block_quote_page(self, supplyDemand: pd.DataFrame, actualSeasonal, industrialProd: pd.DataFrame, growthGdp: pd.DataFrame) -> html.Div:
        return   html.Div(
                [
                    html.Div(
                        [
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
                                className="page-3l",
                            ),
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.Div(
                                                        [
                                                            dcc.Graph(
                                                                figure={
                                                                    "data": [
                                                                        go.Scatter(
                                                                            x=supplyDemand[
                                                                                "Demand, x"
                                                                            ],
                                                                            y=supplyDemand[
                                                                                "Demand, y"
                                                                            ],
                                                                            hoverinfo="y",
                                                                            line={
                                                                                "color": self.color.color_1,
                                                                                "width": 1.5,
                                                                            },
                                                                            name="Demand",
                                                                        ),
                                                                        go.Scatter(
                                                                            x=supplyDemand[
                                                                                "Supply, x; Trace 2, x"
                                                                            ],
                                                                            y=supplyDemand[
                                                                                "Supply, y; Trace 2, y"
                                                                            ],
                                                                            hoverinfo="y",
                                                                            line={
                                                                                "color": self.color.color_2,
                                                                                "width": 1.5,
                                                                            },
                                                                            name="Supply",
                                                                        ),
                                                                    ],
                                                                    "layout": go.Layout(
                                                                        height=250,
                                                                        xaxis={
                                                                            "range": [
                                                                                1988,
                                                                                2015,
                                                                            ],
                                                                            "showgrid": False,
                                                                            "showticklabels": True,
                                                                            "tickangle": -90,
                                                                            "tickcolor": "#b0b1b2",
                                                                            "tickfont": {
                                                                                "family": "Arial",
                                                                                "size": 9,
                                                                            },
                                                                            "tickmode": "linear",
                                                                            "tickprefix": "1Q",
                                                                            "ticks": "",
                                                                            "type": "linear",
                                                                            "zeroline": True,
                                                                            "zerolinecolor": "#FFFFFF",
                                                                        },
                                                                        yaxis={
                                                                            "autorange": False,
                                                                            "linecolor": "#b0b1b2",
                                                                            "nticks": 9,
                                                                            "range": [
                                                                                -3000,
                                                                                5000,
                                                                            ],
                                                                            "showgrid": False,
                                                                            "showline": True,
                                                                            "tickcolor": "#b0b1b2",
                                                                            "tickfont": {
                                                                                "family": "Arial",
                                                                                "size": 9,
                                                                            },
                                                                            "ticks": "outside",
                                                                            "ticksuffix": " ",
                                                                            "type": "linear",
                                                                            "zerolinecolor": "#b0b1b2",
                                                                        },
                                                                        margin={
                                                                            "r": 10,
                                                                            "t": 5,
                                                                            "b": 0,
                                                                            "l": 40,
                                                                            "pad": 2,
                                                                        },
                                                                        hovermode="closest",
                                                                        legend={
                                                                            "x": 0.5,
                                                                            "y": -0.4,
                                                                            "font": {
                                                                                "size": 9
                                                                            },
                                                                            "orientation": "h",
                                                                            "xanchor": "center",
                                                                            "yanchor": "bottom",
                                                                        },
                                                                    ),
                                                                }
                                                            )
                                                        ],
                                                        className="page-3m",
                                                    )
                                                ],
                                                className="six columns",
                                            ),
                                            html.Div(
                                                [
                                                    html.Div(
                                                        [
                                                            dcc.Graph(
                                                                figure={
                                                                    "data": [
                                                                        go.Scatter(
                                                                            x=actualSeasonal[
                                                                                "Actual, x; Crude ex. US SPR, x; Main Products, x"
                                                                            ],
                                                                            y=actualSeasonal[
                                                                                "Actual, y"
                                                                            ],
                                                                            hoverinfo="y",
                                                                            line={
                                                                                "color": "#e41f23",
                                                                                "width": 2,
                                                                            },
                                                                            marker={
                                                                                "maxdisplayed": 0,
                                                                                "opacity": 0,
                                                                            },
                                                                            name="Actual",
                                                                        ),
                                                                        go.Scatter(
                                                                            x=actualSeasonal[
                                                                                "Seasonal*, x"
                                                                            ],
                                                                            y=actualSeasonal[
                                                                                "Seasonal*, y"
                                                                            ],
                                                                            hoverinfo="y",
                                                                            line={
                                                                                "color": self.color.color_3,
                                                                                "dash": "dot",
                                                                                "width": 1.5,
                                                                            },
                                                                            mode="lines",
                                                                            name="Seasonal*",
                                                                        ),
                                                                        go.Bar(
                                                                            x=actualSeasonal[
                                                                                "Actual, x; Crude ex. US SPR, x; Main Products, x"
                                                                            ],
                                                                            y=actualSeasonal[
                                                                                "Crude ex. US SPR, y"
                                                                            ],
                                                                            marker={
                                                                                "color": self.color.color_2
                                                                            },
                                                                            name="Crude ex. US SPR",
                                                                        ),
                                                                        go.Bar(
                                                                            x=actualSeasonal[
                                                                                "Actual, x; Crude ex. US SPR, x; Main Products, x"
                                                                            ],
                                                                            y=actualSeasonal[
                                                                                "Main Products, y"
                                                                            ],
                                                                            marker={
                                                                                "color": self.color.color_1
                                                                            },
                                                                            name="Main Products",
                                                                        ),
                                                                    ],
                                                                    "layout": go.Layout(
                                                                        barmode="relative",
                                                                        dragmode="pan",
                                                                        height=250,
                                                                        width=310,
                                                                        hovermode="closest",
                                                                        legend={
                                                                            "x": 0.06413301662707839,
                                                                            "y": -0.05555227415846632,
                                                                            "bgcolor": "rgba(255, 255, 255, 0)",
                                                                            "borderwidth": 0,
                                                                            "font": {
                                                                                "size": 9
                                                                            },
                                                                            "orientation": "h",
                                                                            "traceorder": "reversed",
                                                                        },
                                                                        margin={
                                                                            "r": 10,
                                                                            "t": 5,
                                                                            "b": 0,
                                                                            "l": 40,
                                                                            "pad": 2,
                                                                        },
                                                                        showlegend=True,
                                                                        titlefont={
                                                                            "size": 16
                                                                        },
                                                                        xaxis={
                                                                            "autorange": True,
                                                                            "range": [
                                                                                0.5,
                                                                                8.5,
                                                                            ],
                                                                            "showgrid": False,
                                                                            "showline": False,
                                                                            "tickcolor": "#b0b1b2",
                                                                            "tickfont": {
                                                                                "family": "Arial",
                                                                                "size": 9,
                                                                            },
                                                                            "tickmode": "array",
                                                                            "ticks": "",
                                                                            "ticktext": [
                                                                                "Jan-15",
                                                                                "Feb-15",
                                                                                "Mar-15",
                                                                                "Apr-15",
                                                                                "May-15",
                                                                                "Jun-15",
                                                                                "Jul-15",
                                                                                "Aug-15",
                                                                            ],
                                                                            "tickvals": [
                                                                                1,
                                                                                2,
                                                                                3,
                                                                                4,
                                                                                5,
                                                                                6,
                                                                                7,
                                                                                8,
                                                                            ],
                                                                            "titlefont": {
                                                                                "size": 8
                                                                            },
                                                                            "type": "linear",
                                                                            "zeroline": True,
                                                                            "zerolinecolor": "#FFFFFF",
                                                                        },
                                                                        xaxis2={
                                                                            "autorange": False,
                                                                            "fixedrange": True,
                                                                            "overlaying": "x",
                                                                            "position": 0.38,
                                                                            "range": [
                                                                                0.5,
                                                                                8.5,
                                                                            ],
                                                                            "showgrid": False,
                                                                            "showticklabels": False,
                                                                            "ticks": "",
                                                                            "ticktext": [
                                                                                "Jan-15",
                                                                                "Feb-15",
                                                                                "Mar-15",
                                                                                "Apr-15",
                                                                                "May-15",
                                                                                "Jun-15",
                                                                                "Jul-15",
                                                                                "Aug-15",
                                                                            ],
                                                                            "tickvals": [
                                                                                1,
                                                                                2,
                                                                                3,
                                                                                4,
                                                                                5,
                                                                                6,
                                                                                7,
                                                                                8,
                                                                            ],
                                                                        },
                                                                        yaxis={
                                                                            "autorange": False,
                                                                            "linecolor": "#b0b1b2",
                                                                            "nticks": 8,
                                                                            "range": [
                                                                                -20,
                                                                                50,
                                                                            ],
                                                                            "showgrid": False,
                                                                            "showline": False,
                                                                            "tickcolor": "#b0b1b2",
                                                                            "tickfont": {
                                                                                "family": "Arial",
                                                                                "size": 9,
                                                                            },
                                                                            "ticks": "outside",
                                                                        },
                                                                    ),
                                                                }
                                                            )
                                                        ],
                                                        className="two columns",
                                                    )
                                                ],
                                                className="page-3m",
                                            ),
                                        ],
                                        className="thirdPage row",
                                    )
                                ],
                                className="page-7",
                            ),
                            html.Div(
                                [
                                    html.P("Bibendum tellus phasellus turpis sapien:"),
                                    html.P(
                                        lorem.paragraph() * 2,
                                        style={
                                            "borderLeft": "5px",
                                            "borderLeftStyle": "solid",
                                            "padding": "30px",
                                            "borderLeftColor": self.color.color_1,
                                            "paddingLeft": "20px",
                                            "borderLeftWidth": "7px",
                                            "backgroundColor": self.color.color_b,
                                        },
                                    ),
                                ],
                                style={
                                    "float": "left",
                                    "marginTop": "20px",
                                    "marginLeft": "30px",
                                },
                                className="eleven columns",
                            ),
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.Strong(
                                                "Ultricies fusce vel, ad ultricies enim, at, egestas",
                                                style={
                                                    "color": self.color.color_1,
                                                    "paddingTop": "100px",
                                                },
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
                                style={
                                    "position": "relative",
                                    "top": "20px",
                                    "marginLeft": "30px",
                                },
                            ),
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            dcc.Graph(
                                                figure={
                                                    "data": [
                                                        go.Scatter(
                                                            x=industrialProd[
                                                                "Industrial Production, x"
                                                            ],
                                                            y=industrialProd[
                                                                "Industrial Production, y"
                                                            ],
                                                            line={"color": self.color.color_2},
                                                            mode="lines",
                                                            name="Industrial Production",
                                                            visible=True,
                                                        ),
                                                        go.Scatter(
                                                            x=industrialProd[
                                                                "Price (rhs), x"
                                                            ],
                                                            y=industrialProd[
                                                                "Price (rhs), y"
                                                            ],
                                                            line={"color": self.color.color_1},
                                                            mode="lines",
                                                            name="Price (rhs)",
                                                            visible=True,
                                                            yaxis="y2",
                                                        ),
                                                    ],
                                                    "layout": go.Layout(
                                                        annotations=[
                                                            {
                                                                "x": 0.95,
                                                                "y": -0.15,
                                                                "arrowhead": 7,
                                                                "ax": 0,
                                                                "ay": -40,
                                                                "font": {"size": 8},
                                                                "showarrow": False,
                                                                "text": "months after shock",
                                                                "xref": "paper",
                                                                "yref": "paper",
                                                            }
                                                        ],
                                                        autosize=True,
                                                        dragmode="pan",
                                                        height=250,
                                                        width=300,
                                                        hovermode="closest",
                                                        legend={
                                                            "x": 0.0,
                                                            "y": 1.2,
                                                            "bgcolor": "rgb(255, 255, 255, 0)",
                                                            "font": {"size": 9},
                                                        },
                                                        margin={
                                                            "r": 40,
                                                            "t": 5,
                                                            "b": 10,
                                                            "l": 20,
                                                            "pad": 0,
                                                        },
                                                        paper_bgcolor="rgb(0, 0, 0, 0)",
                                                        plot_bgcolor="rgb(0, 0, 0, 0)",
                                                        showlegend=True,
                                                        xaxis={
                                                            "autorange": False,
                                                            "nticks": 19,
                                                            "range": [0.5, 18],
                                                            "showgrid": False,
                                                            "tickfont": {
                                                                "color": "rgb(68, 68, 68)",
                                                                "size": 9,
                                                            },
                                                            "ticks": "",
                                                            "type": "linear",
                                                            "zeroline": False,
                                                        },
                                                        yaxis={
                                                            "autorange": False,
                                                            "linecolor": "rgb(190, 191, 192)",
                                                            "mirror": True,
                                                            "nticks": 9,
                                                            "range": [-0.4, 1.2],
                                                            "showgrid": False,
                                                            "showline": True,
                                                            "side": "left",
                                                            "tickfont": {
                                                                "color": "rgb(68, 68, 68)",
                                                                "size": 9,
                                                            },
                                                            "ticks": "outside",
                                                            "ticksuffix": " ",
                                                            "type": "linear",
                                                            "zeroline": False,
                                                        },
                                                        yaxis2={
                                                            "anchor": "x",
                                                            "autorange": False,
                                                            "exponentformat": "e",
                                                            "linecolor": "rgb(190, 191, 192)",
                                                            "nticks": 9,
                                                            "overlaying": "y",
                                                            "range": [-0.1, 0.3],
                                                            "showgrid": False,
                                                            "side": "right",
                                                            "tickfont": {"size": 9},
                                                            "tickprefix": " ",
                                                            "ticks": "outside",
                                                            "type": "linear",
                                                            "zerolinecolor": "rgb(190, 191, 192)",
                                                        },
                                                    ),
                                                }
                                            )
                                        ],
                                        className="six columns",
                                        style={"height": "250px"},
                                    ),
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    dash_table.DataTable(
                                                        data=growthGdp.to_dict("records"),
                                                        columns=[
                                                            {"id": c, "name": c}
                                                            for c in growthGdp.columns
                                                        ],
                                                        style_data_conditional=[
                                                            {
                                                                "if": {"row_index": "odd"},
                                                                "backgroundColor": self.color.color_b,
                                                            },
                                                            {
                                                                "if": {"column_id": ""},
                                                                "backgroundColor": self.color.color_2,
                                                                "color": "white",
                                                            },
                                                        ],
                                                        style_header={
                                                            "backgroundColor": self.color.color_1,
                                                            "fontWeight": "bold",
                                                            "color": "white",
                                                        },
                                                        fixed_rows={"headers": True},
                                                        style_cell={"width": "70px"},
                                                    )
                                                ],
                                                className="exhibit six columns",
                                            )
                                        ],
                                        className="page-2c",
                                    ),
                                ],
                                className="page-7",
                            ),
                        ],
                        className="subpage",
                    )
                ],
                className="page",
            )