# -*- coding: utf-8 -*-
import dash
from dash import dcc,html, dash_table
import plotly.graph_objs as go
import pandas as pd
import lorem
import pathlib
from multi-page-report.scatter_graphs import ScatterGraph, MultipleScatterGraph, MultipleYScatterGraph, create_energy_line_scatter, create_producer_scatter_graph


class MultiPageOptions:
    def __init__(self):
        self.title = "My Multipage Report"
        self.author = "John Doe"
        self.logo_path = "logo.png"
        self.page_titles = ["Page 1", "Page 2", "Page 3"]
        self.page_layouts = [
            html.Div(
                [
                    html.H1("Page 1"),
                    dcc.Graph(
                        figure={
                            "data": [{"x": [1, 2, 3], "y": [4, 1, 2], "type": "bar"}],
                            "layout": {"title": "Page 1 Plot"},
                        }
                    ),
                ]
            ),
            html.Div(
                [
                    html.H1("Page 2"),
                    dcc.Graph(
                        figure={
                            "data": [{"x": [1, 2, 3], "y": [1, 4, 3], "type": "bar"}],
                            "layout": {"title": "Page 2 Plot"},
                        }
                    ),
                ]
            ),
            html.Div(
                [
                    html.H1("Page 3"),
                    dcc.Graph(
                        figure={
                            "data": [{"x": [1, 2, 3], "y": [3, 2, 4], "type": "bar"}],
                            "layout": {"title": "Page 3 Plot"},
                        }
                    ),
                ]
            ),
        ]


class MultiPageDataLoader:
    def __init__(self, base_path="multi-page-report/report-example"):
        self.BASE_PATH = pathlib.Path(base_path).resolve()
        self.DATA_PATH = self.BASE_PATH.joinpath("Data").resolve()

    def load_data(self, filename):
        return pd.read_csv(self.DATA_PATH.joinpath(filename))
    
    # def get_example_data(self):


class ColorManager:
    def __init__(self):
        self.color_1 = "#003399"
        self.color_2 = "#00ffff"
        self.color_3 = "#002277"
        self.color_b = "#F8F8FF"

class MultiPageReport:
    def __init__(self, options=MultiPageOptions, data_loader=MultiPageDataLoader, color_manager=ColorManager):
        self.options = options()
        self.data_loader = data_loader()
        self.color = color_manager()

    def generate_multipage_report(self, app):
        options = MultiPageOptions()
        # Path
        BASE_PATH = pathlib.Path("multi-page-report/report-example").resolve()
        DATA_PATH = BASE_PATH.joinpath("Data").resolve()

        ## Read in data
        ## Eventually each of these will be attached to a specific class 
        ## Supply Demand Line Chart
        supplyDemand = pd.read_csv(DATA_PATH.joinpath("supplyDemand.csv"))
        ### Seasonal Graph Compound Bar and Lines Chart
        actualSeasonal = pd.read_csv(DATA_PATH.joinpath("actualSeasonal.csv"))

        ### Industrail Production Line Chart
        industrialProd = pd.read_csv(DATA_PATH.joinpath("industrialProd.csv"))

        ### Global Market Line Chart    
        globalMarket = pd.read_csv(DATA_PATH.joinpath("globalMarket.csv"))
        ### OECD Commersial Line Chart
        oecdCommercial = pd.read_csv(DATA_PATH.joinpath("oecdCommercial.csv"))
        ### WTI Prices & Forecast Line Chart & Table
        wtiPrices = pd.read_csv(DATA_PATH.joinpath("wtiPrices.csv"))
        ### EPX Equity Line Chart
        epxEquity = pd.read_csv(DATA_PATH.joinpath("epxEquity.csv"))
        chinaSpr = pd.read_csv(DATA_PATH.joinpath("chinaSpr.csv"))
        oecdIndustry = pd.read_csv(DATA_PATH.joinpath("oecdIndustry.csv"))
        wtiOilprices = pd.read_csv(DATA_PATH.joinpath("wtiOilprices.csv"))
        productionCost = pd.read_csv(DATA_PATH.joinpath("productionCost.csv"))
        production2015 = pd.read_csv(DATA_PATH.joinpath("production2015.csv"))
        energyShare = pd.read_csv(DATA_PATH.joinpath("energyShare.csv"))
        adjustedSales = pd.read_csv(DATA_PATH.joinpath("adjustedSales.csv"))
        ### Growth GDP Table
        growthGdp = pd.read_csv(DATA_PATH.joinpath("growthGdp.csv"))

        app = dash.Dash(__name__)
        app.title = options.title

        server = app.server

        app.layout = html.Div(
            children=[
                self.create_pg1(app),
                self.create_pg2(app),
                self.create_pg3(app),
                self.create_pg4(app, supplyDemand=supplyDemand, actualSeasonal=actualSeasonal, industrialProd=industrialProd, growthGdp=growthGdp),
                self.create_pg5(app, globalMarket=globalMarket, oecdCommercial=oecdCommercial),
                self.create_pg6(app, wtiPrices=wtiPrices),
                self.create_pg7(app, epxEquity=epxEquity),
                self.create_pg8(app),
                self.create_pg9(app, chinaSpr=chinaSpr),
                self.create_pg10(app, oecdIndustry=oecdIndustry, productionCost=productionCost, production2015=production2015, wtiOilprices=wtiOilprices),
                self.create_pg11(app, energyShare=energyShare),
                self.create_pg12(app, adjustedSales=adjustedSales),
            ]
        )
        return app
    
    def create_text_block(self, header_text: str, num_paragraphs: int) -> html.Div:
        """
        Creates a text block with a header and one or more paragraphs of lorem ipsum text.

        Args:
            header_text (str): The text to use as the header for the text block.
            num_paragraphs (int): The number of paragraphs of lorem ipsum text to include in the block.

        Returns:
            html.Div: A Div element containing the header and paragraphs of text.
        """
        return html.Div(
            [
                html.H6(header_text, className="page-1h"),
                html.P(lorem.paragraph() * num_paragraphs),
            ],
            className="page-1k",
        )


    def create_pg1(self, app: dash.Dash) -> html.Div:
        """
        Creates the layout for the first page of the multipage report.

        Args:
            app (dash.Dash): The Dash app instance.

        Returns:
            html.Div: The layout for the first page of the report.
        """
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
                                                            html.Img(
                                                                src=app.get_asset_url(
                                                                    "dash-logo-new.png"
                                                                ),
                                                                className="page-1a",
                                                            )
                                                        ),
                                                        html.Div(
                                                            [
                                                                html.H6("Suscipit nibh"),
                                                                html.H5("LOREM IPSUM DOLOR"),
                                                                html.H6("Blandit pretium dui"),
                                                            ],
                                                            className="page-1b",
                                                        ),
                                                    ],
                                                    className="page-1c",
                                                )
                                            ],
                                            className="page-1d",
                                        ),
                                        html.Div(
                                            [
                                                html.H1(
                                                    [
                                                        html.Span("03", className="page-1e"),
                                                        html.Span("19"),
                                                    ]
                                                ),
                                                html.H6("Suscipit nibh vita"),
                                            ],
                                            className="page-1f",
                                        ),
                                    ],
                                    className="page-1g",
                                ),
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.H6("Report Author", className="page-1h"),
                                                html.P("555-555-5555"),
                                                html.P("author@report.com"),
                                            ],
                                            className="page-1i",
                                        ),
                                        html.Div(
                                            [
                                                html.H6("Report Name", className="page-1h"),
                                                html.P("06/04/2023"),
                                                html.P("Report ID: 123456"),
                                                html.P("Report Period: 5/1/2023-5/31/2023"),
                                            ],
                                            className="page-1i",
                                        ),
                                        
                                    ],
                                    className="page-1j",
                                ),
                                html.Div(
                                    [
                                        self.create_text_block("A elementum lorem dolor aliquam nisi diam", 2),
                                        self.create_text_block("A elementum lorem dolor aliquam nisi diam", 2),
                                        self.create_text_block("A elementum lorem dolor aliquam nisi diam", 1),
                                        self.create_text_block("A elementum lorem dolor aliquam nisi diam", 1),
                                    ],
                                    className="page-1n",
                                ),
                            ],
                            className="subpage",
                        )
                    ],
                    className="page",
                )
    
    def create_pg2(self, app) -> html.Div:
        return html.Div(
                    [
                        html.Div(
                            [
                                html.Div([html.H1("Report Summary")], className="page-2a"),
                                html.Div(
                                    [
                                        html.P(lorem.paragraph() * 3, className="page-2b"),
                                        html.P(lorem.paragraph() * 2, className="page-2c"),
                                        html.P(lorem.paragraph() * 2, className="page-2c"),
                                    ],
                                    className="page-3",
                                ),
                                html.Div(
                                    [
                                        html.P(lorem.paragraph() * 2, className="page-2b"),
                                        html.P(lorem.paragraph() * 3, className="page-2c"),
                                    ],
                                    className="page-3",
                                ),
                            ],
                            className="subpage",
                        )
                    ],
                    className="page",
                )
    
    def create_pg3(self, app) -> html.Div:
        return  html.Div([
                    html.Div(
                        [
                            html.Div([html.H1("LOREM IPSUM")], className="page-3a"),
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.H6(
                                                        "Mauris feugiat quis lobortis nisl sed",
                                                        className="page-3b",
                                                    ),
                                                    html.P(
                                                        lorem.paragraph(),
                                                        className="page-3c",
                                                    ),
                                                ]
                                            ),
                                            html.Div(
                                                [
                                                    html.Div(
                                                        [
                                                            html.P(
                                                                lorem.paragraph() * 2,
                                                                className="page-3d",
                                                            )
                                                        ],
                                                        className="page-3e",
                                                    ),
                                                    html.Div(
                                                        [
                                                            html.P(
                                                                lorem.paragraph() * 2,
                                                                className="page-3d",
                                                            )
                                                        ],
                                                        className="page-3f",
                                                    ),
                                                    html.Div(
                                                        [
                                                            html.P(
                                                                lorem.paragraph(),
                                                                className="page-3d",
                                                            )
                                                        ],
                                                        className="page-3g",
                                                    ),
                                                ],
                                                className="page-3i",
                                            ),
                                            html.Div(
                                                [
                                                    html.P(
                                                        lorem.paragraph(),
                                                        className="page-2c",
                                                    )
                                                ]
                                            ),
                                        ],
                                        className="page-3j",
                                    )
                                ]
                            ),
                        ],
                        className="subpage",
                    )
                ],
                className="page",
            )

    def create_pg4(self, app, supplyDemand: pd.DataFrame, actualSeasonal, industrialProd: pd.DataFrame, growthGdp: pd.DataFrame) -> html.Div:
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
            
    def create_pg5(self, app, globalMarket: pd.DataFrame, oecdCommercial) -> html.Div:
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
                                            html.Div(
                                                [html.P(lorem.paragraph())],
                                                className="page-5",
                                            ),
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
            
    def create_pg6(self, app, wtiPrices: pd.DataFrame) -> html.Div:
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
                                                    "At velit pharetra ac fusce sit dictum pellentesque",
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
            
    def create_pg7(self, app, epxEquity) -> html.Div:
    # Page 7
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
                                                    "Vehicula elementum congue penatibus massa, eu sed sed dolor",
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
        
    def create_pg8(self,app):
         # Page 8
        return  html.Div(
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
                                                            html.H6(
                                                                "Aliquet ut mauris nostra habitant egestas, massa vulputate. Magnis nullam leo eget ullamcorper lacus congue laoreet ex sed",
                                                                className="page-3b",
                                                            ),
                                                            html.P(
                                                                lorem.paragraph(),
                                                                className="page-3c",
                                                            ),
                                                            html.P(
                                                                lorem.paragraph(),
                                                                className="page-8a",
                                                            ),
                                                        ]
                                                    ),
                                                    html.Div(
                                                        [
                                                            html.Div(
                                                                [
                                                                    html.P(
                                                                        lorem.paragraph()
                                                                        * 2,
                                                                        className="page-3d",
                                                                    )
                                                                ],
                                                                className="page-3e",
                                                            ),
                                                            html.Div(
                                                                [
                                                                    html.P(
                                                                        lorem.paragraph()
                                                                        * 2,
                                                                        className="page-3d",
                                                                    )
                                                                ],
                                                                className="page-3f",
                                                            ),
                                                            html.Div(
                                                                [
                                                                    html.P(
                                                                        lorem.paragraph()
                                                                        * 2,
                                                                        className="page-3d",
                                                                    )
                                                                ],
                                                                className="page-3g",
                                                            ),
                                                        ],
                                                        className="page-3i",
                                                    ),
                                                    html.Div(
                                                        [
                                                            html.P(
                                                                lorem.paragraph(),
                                                                className="page-2c",
                                                            )
                                                        ]
                                                    ),
                                                ],
                                                className="nine columns",
                                            )
                                        ],
                                        className="page-8b",
                                    )
                                ],
                                className="subpage",
                            )
                        ],
                        className="page-8c",
                    )
                ],
                className="page",
            )
                
    def create_pg9(self,app, chinaSpr: pd.DataFrame):
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
                                                            "Aenean felis et libero nullam pretium quis est in sit. Commodo nec ante aenean a. Commodo at facilisis vestibulum cursus elementum nascetur et, placerat class aliquam convallis porttitor accumsan. Ultricies sed laoreet eleifend maximus venenatis",
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
                                                                                x=chinaSpr[
                                                                                    "OECD commercial ex. US NGL & other, x"
                                                                                ],
                                                                                y=chinaSpr[
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
                                                                                x=chinaSpr[
                                                                                    "Non-OECD stocks ex. China SPR, x"
                                                                                ],
                                                                                y=chinaSpr[
                                                                                    "Non-OECD stocks ex. China SPR, y"
                                                                                ],
                                                                                line={
                                                                                    "color": self.color.color_2,
                                                                                    "width": 2,
                                                                                },
                                                                                mode="lines",
                                                                                name="Non-OECD stocks ex. China SPR",
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
    
    def create_pg10(self, app, oecdIndustry: pd.DataFrame, productionCost, production2015, wtiOilprices):
        producer_scatter_graph = create_producer_scatter_graph(production2015)
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
                                                html.Strong(
                                                    "Nulla diam conubia nec lacus urna in ligula nec ut egestas sed. Diam inceptos nec venenatis",
                                                    className="page-3h",
                                                ),
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
    
    def create_pg11(self,app, energyShare: pd.DataFrame):
        
        energy_line_scatter = create_energy_line_scatter(energyShare)

        return html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.H6(
                                    "In tempor mauris non, maximus non odio. Lacus mi arcu, ut parturient ac sed curae \
                                    sed litora amet quam, massa purus condimentum",
                                    className="page-9h",
                                ),
                                html.P(lorem.paragraph() * 2, className="page-9f"),
                                html.P(lorem.paragraph(), className="page-9g"),
                                html.P(lorem.paragraph() * 3, className="page-9f"),
                            ],
                            className="twelve columns",
                        ),
                        energy_line_scatter],
                    className="subpage",
                )
            ],
            style={"marginTop": "50px"},
            className="page",
        )

                

    def create_pg12(self,app, adjustedSales: pd.DataFrame):
            # Page 12
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.H6(
                                                "Erat cras porta inceptos nibh sociis justo. Natoque mauris nunc etiam, dis quam, tempor consectetur ac \
                                        Pulvinar nunc vitae dui elit hac ante, facilisi, primis nascetur. Non nostra torquent ipsum ac amet",
                                                className="page-9h",
                                            ),
                                            html.P(lorem.paragraph(), className="page-1i"),
                                            html.P(lorem.paragraph(), className="page-1i"),
                                            html.H6(
                                                "Ultrices phasellus dignissim, accumsan platea volutpat, sapien mi enim. Pharetra ipsum netus in turpis, \
                                        lorem tempus et. Eget sed. Eu porta cum tempor convallis sed nostra, pellentesque eros.",
                                                className="page-6c",
                                            ),
                                            html.Div(
                                                [
                                                    dash_table.DataTable(
                                                        data=adjustedSales.to_dict(
                                                            "records"
                                                        ),
                                                        columns=[
                                                            {"id": c, "name": c}
                                                            for c in adjustedSales.columns
                                                        ],
                                                        style_data_conditional=[
                                                            {
                                                                "if": {"row_index": "odd"},
                                                                "backgroundColor": self.color.color_b,
                                                            },
                                                            {
                                                                "if": {
                                                                    "column_id": "Quarter"
                                                                },
                                                                "backgroundColor": self.color.color_2,
                                                                "color": "black",
                                                            },
                                                        ],
                                                        style_header={
                                                            "backgroundColor": self.color.color_1,
                                                            "fontWeight": "bold",
                                                            "color": "white",
                                                        },
                                                        fixed_rows={"headers": True},
                                                        style_cell={"width": "150px"},
                                                    )
                                                ],
                                                className="page-1i",
                                            ),
                                        ],
                                        className="eleven columns",
                                    )
                                ],
                                className="page-12a",
                            )
                        ],
                        className="subpage",
                    )
                ],
                className="page",
            )


