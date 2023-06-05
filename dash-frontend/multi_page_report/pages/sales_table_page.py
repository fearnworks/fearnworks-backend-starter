from dash import html, dcc, dash_table
from .page_utils import PageUtils
import pandas as pd
import plotly.graph_objects as go
import lorem

class SalesTablePage:
    """
    A class representing a sales table page for a report.
    """

    def __init__(self, color, adjustedSales: pd.DataFrame):
        """
        Initializes a new instance of the ForecastPage class.

        Args:
            color (str): The color scheme to use for the page. 
            wtiPrices (pd.DataFrame): A DataFrame containing WTI prices and forecasts.
        """
        self.utils = PageUtils()
        self.color = color
        self.layout = self.create_sales_table_page(adjustedSales)


    def create_sales_table_page(self,adjustedSales: pd.DataFrame):
        """
        Creates a Dash layout for the sales table page.

        Args :
            adjustedSales (pd.DataFrame): A DataFrame containing adjusted sales data.

        Returns:
            A Dash layout for the sales table page.
        """
        return html.Div(
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


