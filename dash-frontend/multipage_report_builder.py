# -*- coding: utf-8 -*-
import dash
from dash import dcc,html, dash_table
import plotly.graph_objs as go
import pandas as pd
import lorem
import pathlib
from multi_page_report.scatter_graphs import create_energy_line_scatter, create_producer_scatter_graph, build_production_scatter
import multi_page_report.pages as MPR_Pages

class MultiPageOptions:
    def __init__(self):
        self.title = "Example Report"
        self.author = "John Doe"
        self.logo_file = "dash-logo-new.png"
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
    def __init__(self, base_path="multi_page_report/report-example"):
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

class MultiPageReportBuilder:
    def __init__(self, options=MultiPageOptions, data_loader=MultiPageDataLoader, color_manager=ColorManager):
        self.options = options()
        self.data_loader = data_loader()
        self.color = color_manager()
        self.utils = MPR_Pages.PageUtils()

    def encode_logo(self, app, logo_file: str):
        return html.Img(
            src=app.get_asset_url(
                logo_file
            ),
            className="page-1a",
        )

    def generate_multipage_report(self, app):
        options = MultiPageOptions()
        # Path
        BASE_PATH = pathlib.Path("multi_page_report/report-example").resolve()
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
        forSpr = pd.read_csv(DATA_PATH.joinpath("forSpr.csv"))
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

        ## Cover page takes in : def __init__(self, img_path: str, title: str, subtitle: str, author: str, report_name: str, report_id: str, report_period: str)
        cover_logo = self.encode_logo(app, options.logo_file)
        self.cover_page = MPR_Pages.CoverPage(logo=cover_logo, subtitle="An example report", author=options.author, report_name=options.title, report_id="R-001", report_period="05/01/23-05/31/23", delivery_date="06/05/2023")
        self.summary_page = MPR_Pages.SummaryPage("default")
        self.summary_page_alt = MPR_Pages.SummaryPage("alt")
        self.graph_and_block_quote_page = MPR_Pages.GraphAndBlockQuotePage(self.color, supplyDemand, actualSeasonal, industrialProd, growthGdp)
        self.anomaly_analysis_page = MPR_Pages.AnomalyAnalysisPage(self.color, oecdIndustry, productionCost, production2015, wtiOilprices)
        self.global_market_page = MPR_Pages.GlobalMarketPage(self.color, globalMarket, oecdCommercial)
        self.forecast_page = MPR_Pages.ForecastPage(self.color, app, wtiPrices)
        self.supply_reserve_page = MPR_Pages.SupplyReserveAnalysisPage(self.color, app, forSpr)
        self.sales_table_page = MPR_Pages.SalesTablePage(self.color, adjustedSales)
        self.bond_analysis_page = MPR_Pages.BondAnalysisPage(self.color, epxEquity)
        self.rig_to_yield_page = MPR_Pages.RigToYieldPage(self.color, energyShare)

        app.layout = html.Div(
            children=[
                self.cover_page.layout,
                self.summary_page.layout,
                self.summary_page_alt.layout,
                self.graph_and_block_quote_page.layout,
                self.global_market_page.layout,
                self.forecast_page.layout,
                self.bond_analysis_page.layout,
                self.supply_reserve_page.layout,
                self.anomaly_analysis_page.layout,
                self.rig_to_yield_page.layout,
                self.sales_table_page.layout,
            ]
        )
        return app
    

            
         
        
    

    