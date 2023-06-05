
from dash import html, dcc, dash_table
from .page_utils import PageUtils
import pandas as pd
import plotly.graph_objects as go
import lorem
from ..scatter_graphs import create_energy_line_scatter

class RigToYieldPage:
    """
    A class representing a rig to yield analysis
    """

    def __init__(self, color, energyShare: pd.DataFrame):
        """
        Initializes a new RTY page

        Args:
            color (str): The color scheme to use for the page. 
            energyShare (pd.DataFrame): A DataFrame containing energy share data.
        """
        self.utils = PageUtils()
        self.color = color
        self.layout = self.create_rig_to_yield_analsysis(energyShare)

    def create_rig_to_yield_analsysis(self, energyShare: pd.DataFrame):
        
        energy_line_scatter = create_energy_line_scatter(energyShare, self.color)

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

                