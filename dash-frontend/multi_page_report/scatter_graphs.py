import plotly.graph_objs as go
from dash import dcc, html
import pandas as pd 

class ScatterGraph:
    def __init__(self):
        pass  # No initialization needed for this class

    def create_scatter(self, x_data, y_data, marker_color=None, marker_symbol=None, mode="lines", name=None, yaxis="y"):
        return go.Scatter(
            x=x_data,
            y=y_data,
            marker={
                "color": marker_color if marker_color else "rgb(171, 172, 173)",
                "symbol": marker_symbol if marker_symbol else "circle",
            },
            mode=mode,
            name=name,
            yaxis=yaxis,
            visible=True,
        )

    def create(self, scatter_data, layout_config, className=None):
        return html.Div(
            [
                dcc.Graph(
                    figure={
                        "data": scatter_data,
                        "layout": go.Layout(**layout_config),
                    }
                )
            ],
            className=className
        )
 #### Deprecating ####   
class MultipleScatterGraph:
    def __init__(self):
        pass  # No initialization needed for this class

    def create_scatter(self, x_data, y_data, marker_color, marker_symbol, mode, name):
        return go.Scatter(
            x=x_data,
            y=y_data,
            marker={
                "color": marker_color,
                "symbol": marker_symbol,
            },
            mode=mode,
            name=name,
            visible=True,
        )

    def create(self, scatter_data, layout_config, className=None):
        return html.Div(
            [
                dcc.Graph(
                    figure={
                        "data": scatter_data,
                        "layout": go.Layout(**layout_config),
                    }
                )
            ],
            className=className
        )
    
class MultipleYScatterGraph:
    def __init__(self):
        pass

    def create_scatter(self, x_data: pd.DataFrame, y_data: pd.DataFrame, marker_color: str, marker_symbol: str, mode: str, name: str, yaxis: str = "y") -> go.Scatter:
        """
        Creates a scatter plot trace.

        Args:
            x_data (pd.DataFrame): A Pandas DataFrame containing the x-axis data for the scatter plot.
            y_data (pd.DataFrame): A Pandas DataFrame containing the y-axis data for the scatter plot.
            marker_color (str): The color of the markers in the scatter plot.
            marker_symbol (str): The symbol used for the markers in the scatter plot.
            mode (str): The mode of the scatter plot (e.g. "markers", "lines", "lines+markers").
            name (str): The name of the scatter plot trace.
            yaxis (str, optional): The y-axis to use for the scatter plot. Defaults to "y".

        Returns:
            go.Scatter: A Plotly scatter plot trace.
        """
        return go.Scatter(
            x=x_data,
            y=y_data,
            marker={
                "color": marker_color,
                "symbol": marker_symbol,
            },
            mode=mode,
            name=name,
            yaxis=yaxis,
            visible=True,
        )

    def create(self, scatter_data: list, layout_config: dict, className: str = None) -> html.Div:
        """
        Creates a Dash Div element containing a Plotly scatter plot.

        Args:
            scatter_data (list): A list of Plotly scatter plot traces.
            layout_config (dict): A dictionary of Plotly layout configuration options.
            className (str, optional): The CSS class name to apply to the Div element. Defaults to None.

        Returns:
            html.Div: A Dash Div element containing the scatter plot.
        """
        return html.Div(
            [
                dcc.Graph(
                    figure={
                        "data": scatter_data,
                        "layout": go.Layout(**layout_config),
                    }
                )
            ],
            className=className
        )
#### Specific to this report

def build_production_scatter(x_data, y_data):
    # Initialize the class
    scatter_graph = ScatterGraph()

    # Create the scatter data
    scatter_data = scatter_graph.create_scatter(
        x_data=x_data, 
        y_data=y_data, 
        marker_color="rgb(171, 172, 173)", 
        marker_symbol="circle", 
        mode="lines", 
        name="My Scatter Plot"
    )

    # Define the layout configuration
    layout_config = {
        "height": 200,
        "margin": {"r": 20, "t": 10, "b": 50, "l": 40},
        "xaxis": {
            "autorange": False,
            "exponentformat": "none",
            "linecolor": "rgb(171, 172, 173)",
            "nticks": 5,
            "range": [0, 40000],
            "showgrid": False,
            "showline": True,
            "tickfont": {"size": 9},
            "ticks": "outside",
            "title": "Cumulative peak oil production (kb/d)",
            "titlefont": {"size": 9},
            "type": "linear",
            "zeroline": False,
        },
        "yaxis": {
            "autorange": False,
            "linecolor": "rgb(171, 172, 173)",
            "nticks": 10,
            "range": [0, 45],
            "showgrid": False,
            "showline": True,
            "tickfont": {"size": 9},
            "ticks": "outside",
            "title": "Production cost (US$/bbl)",
            "titlefont": {"size": 9},
            "type": "linear",
            "zeroline": False,
        },
    }

    # Create the scatter plot
    return scatter_graph.create(scatter_data, layout_config)

class Color:
    color_1: str
    color_2: str
    color_3: str
    color_b: str

def create_energy_line_scatter(data: pd.DataFrame, color: Color) -> html.Div:
    scatter_graph = MultipleYScatterGraph()
    energyShare = data
    energy_scatter_data = [
        scatter_graph.create_scatter(
            energyShare["Energy share of HY Issuance, x"],
            energyShare["Energy share of HY Issuance, y"],
            color.color_1,
            "diamond",
            "lines",
            "Energy share of HY Issuance"
        ),
        scatter_graph.create_scatter(
            energyShare["US oil rig count  (monthly change), x"],
            energyShare["US oil rig count  (monthly change), y"],
            color.color_2,
            "diamond",
            "lines",
            "US oil rig count  (monthly change)",
            yaxis="y2"
        ),
    ]

    energy_scatter_layout_config = {
        "height": 300,
        "autosize": True,
        "hovermode": "closest",
        "legend": {
            "x": 0.39727646537238737,
            "y": -0.12197967025477964,
            "bgcolor": "rgba(255, 255, 255, 0)",
            "font": {
                "color": "rgb(68, 68, 68)",
                "size": 9,
            },
            "orientation": "h",
            "traceorder": "reversed",
        },
        "margin": {
            "r": 30, 
            "t": 10, 
            "b": 0, 
            "l": 30
        },
        "showlegend": True,
        "xaxis": {
            "autorange": True,
            "nticks": 10,
            "range": [-0.007132542, 8.1854778101],
            "showgrid": False,
            "tickfont": {
                "size": 9
            },
            "ticks": "",
            "ticktext": [
                " Jan-13",
                "  May-13",
                "  Sep-13",
                "  Jan-14",
                "  May-14",
                "  Sep-14",
                "  Jan-15",
                "  May-15",
            ],
            "tickvals": [0, 1, 2, 3, 4, 5, 6, 7],
            "title": "",
            "type": "linear",
            "zeroline": True,
            "zerolinecolor": "rgb(171, 172, 173)",
            "zerolinewidth": 1,
        },
        "yaxis": {
            "autorange": False,
            "linecolor": "rgb(136, 137, 140)",
            "nticks": 10,
            "range": [-300, 150],
            "showgrid": False,
            "showline": False,
            "tickfont": {
                "size": 9
            },
            "ticks": "outside",
            "title": "",
            "type": "linear",
            "zeroline": True,
            "zerolinecolor": "rgb(171, 172, 173)",
            "zerolinewidth": 1,
        },
        "yaxis2": {
            "anchor": "x",
            "autorange": False,
            "linecolor": "rgb(136, 137, 140)",
            "nticks": 8,
            "overlaying": "y",
            "range": [0, 35],
            "showgrid": False,
            "showline": True,
            "side": "right",
            "tickfont": {
                "size": 9
            },
            "ticks": "outside",
            "ticksuffix": " %",
            "type": "linear",
            "zeroline": False,
            "zerolinecolor": "rgb(171, 172, 173)",
            "zerolinewidth": 1,
        },
    }
    return scatter_graph.create(energy_scatter_data, energy_scatter_layout_config, className="eleven columns")

def create_producer_scatter_graph(production2015, color: Color) -> html.Div:
        scatter_graph = MultipleScatterGraph()

        scatter_data = [
            scatter_graph.create_scatter(
                production2015["Canadian Producers, x"], 
                production2015["Canadian Producers, y"], 
                "rgb(255, 0, 0)", 
                "diamond", 
                "markers", 
                "Canadian Producers"
            ),
            scatter_graph.create_scatter(
                production2015["US E&Ps and Integrated, x"], 
                production2015["US E&Ps and Integrated, y"], 
                color.color_2, 
                "diamond", 
                "markers", 
                "US E&Ps and Integrated"
            ),
            scatter_graph.create_scatter(
                production2015["Others, x"], 
                production2015["Others, y"], 
                color.color_1, 
                "diamond", 
                "markers", 
                "Others"
            ),
        ]

        layout_config = {
            "height": 200,
            "autosize": True,
            "hovermode": "closest",
            "legend": {
                "x": -0.06,
                "y": -0.36,
                "font": {
                    "size": 9
                },
                "orientation": "h",
            },
            "margin": {
                "r": 10,
                "t": 10,
                "b": 0,
                "l": 40,
            },
            "showlegend": True,
            "xaxis": {
                "autorange": False,
                "nticks": 8,
                "range": [0, 100],
                "showgrid": False,
                "showline": True,
                "tickfont": {
                    "size": 9
                },
                "ticks": "outside",
                "ticksuffix": "%",
                "titlefont": {
                    "size": 9
                },
                "title": "2015 Net Debt / Capital Employed",
                "type": "linear",
                "zeroline": False,
            },
            "yaxis": {
                "autorange": False,
                "nticks": 12,
                "range": [0, 45],
                "showgrid": False,
                "showline": True,
                "tickfont": {
                    "size": 9
                },
                "ticks": "outside",
                "title": "2015 Production Cost $/bbl",
                "titlefont": {
                    "size": 9
                },
                "type": "linear",
                "zeroline": True,
            },
        }

        return scatter_graph.create(scatter_data, layout_config, "six columns")
