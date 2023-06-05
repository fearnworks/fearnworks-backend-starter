from dash import html
from .page_utils import PageUtils

class CoverPage:
    """
    A class representing a cover page for a report.

    Methods:
        create_cover_page: Creates a Dash layout for the cover page.
    """

    def __init__(self, logo: html.Img, subtitle: str, author: str, report_name: str, report_id: str, report_period: str, delivery_date: str):
        """
        Initializes a new instance of the CoverPage class.

        Args:
            logo (html.IMG): The logo to use for cover header
            subtitle (str): The subtitle of the report.
            author (str): The author of the report.
            report_name (str): The name of the report.
            report_id (str): The ID of the report.
            report_period (str): The reporting period for the report.
            delivery_date (str): The delivery date of the report.
        """
        self.utils = PageUtils()
        header = self.create_cover_header(logo, report_name, subtitle)
        self.layout = self.create_cover_page(header, author, report_name, report_id, report_period, delivery_date)

    def create_cover_page(self, cover_header: html.Div, author, report_name, report_id, report_period, delivery_date):
        """
        Creates a Dash layout for the cover page.

        Args:
            cover_header (html.Div): The header for the cover page.
            title (str): The title of the report.
            subtitle (str): The subtitle of the report.
            author (str): The author of the report.
            report_name (str): The name of the report.
            report_id (str): The ID of the report.
            report_period (str): The reporting period for the report.
            delivery_date (str): The delivery date of the report.

        Returns:
            A Dash layout for the cover page.
        """
        return html.Div(
            [
                html.Div(
                    [
                        cover_header,
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H6("Report Author", className="page-1h"),
                                        html.P(author),
                                    ],
                                    className="page-1i",
                                ),
                                html.Div(
                                    [
                                        html.H6(report_name, className="page-1h"),
                                        html.P(delivery_date),
                                        html.P(f"Report ID: {report_id}"),
                                        html.P(f"Report Period: "),
                                        html.P(report_period),
                                    ],
                                    className="page-1i",
                                ),
                            ],
                            className="page-1j",
                        ),
                        html.Div(
                            [
                                self.utils.create_text_block("A elementum lorem dolor aliquam nisi diam", 2),
                                self.utils.create_text_block("A elementum lorem dolor aliquam nisi diam", 2),
                                self.utils.create_text_block("A elementum lorem dolor aliquam nisi diam", 1),
                                self.utils.create_text_block("A elementum lorem dolor aliquam nisi diam", 1),
                            ],
                            className="page-1n",
                        ),
                    ],
                    className="subpage",
                )
            ],
            className="page",
        )
    
    def create_cover_header(self, logo, report_name, subtitle) -> html.Div:
        return html.Div(
                            [
                                html.Div(
                                    [
                                        logo,
                                        html.Div(
                                            [
                                                html.H6(report_name),
                                                html.H5(subtitle),
                                                html.H6("Blandit pretium dui"),
                                            ],
                                            className="page-1b",
                                        ),
                                    ],
                                    className="page-1c",
                                )
                            ],
                            className="page-1d",
                        )
    