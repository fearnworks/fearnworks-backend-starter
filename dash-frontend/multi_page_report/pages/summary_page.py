from dash import html
from .page_utils import PageUtils
import lorem 

class SummaryPage:
    """
    A class representing a summary page for a report.

    Attributes:
        page_type (str): The type of summary page to create.

    Methods:
        create_summary_page: Creates a Dash layout for the summary page.
    """

    def __init__(self,page_type):
        """
        Initializes a new instance of the SummaryPage class.

        Args:
            page_type (str): The type of summary page to create.
        """

        self.utils = PageUtils()
        self.page_type = page_type
        self.layout = self.create_summary_page()

    def create_summary_page(self):
        """
        Creates a Dash layout for the summary page.

        Returns:
            A Dash layout for the summary page.
        """
        if self.page_type == "default":
            # Create a default summary page layout
            return self.default_summary()
        elif self.page_type == "alt":
            # Create an alternate summary page layout
            return self.alt_summary()
        else:
            raise ValueError(f"Invalid summary page type: {self.page_type}")
        
    def default_summary(self):
        return html.Div(
                    [
                        html.Div(
                            [
                                html.Div([html.H1("Report Summary")], className="page-2a"),
                                html.Div(
                                    [
                                        self.utils.create_paragraph(2, className="page-2b"),
                                        self.utils.create_paragraph(2, className="page-2c"),
                                        self.utils.create_paragraph(2,  className="page-2c"),
                                    ],
                                    className="page-3",
                                ),
                                html.Div(
                                    [
                                        self.utils.create_paragraph(2,  className="page-2b"),
                                        self.utils.create_paragraph(2,  className="page-2c"),
                                    ],
                                    className="page-3",
                                ),
                            ],
                            className="subpage",
                        )
                    ],
                    className=
                    "page",
                )
    
    def alt_summary(self):
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
                                            self.utils.create_paragraph(2, className="page-3c",
                                            ),
                                        ]
                                    ),
                                    html.Div(
                                        [
                                            html.Div(
                                                [self.utils.create_paragraph(2, className="page-3d",)],
                                                className="page-3e",
                                            ),
                                            html.Div(
                                                [self.utils.create_paragraph(2,className="page-3d",)],className="page-3f",),
                                            html.Div(
                                                [self.utils.create_paragraph(2, className="page-3d", )
                                                ],
                                                className="page-3g",
                                            ),
                                        ],
                                        className="page-3i",
                                    ),
                                    html.Div(
                                        [self.utils.create_paragraph(2, className="page-2c",)]),],
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