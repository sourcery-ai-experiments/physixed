import plotly.graph_objs as go
import numpy as np


def make_plot(x_data: list, y_data: list, x_label: str, y_label: str) -> str:
    """
    Create a interactive line plot with the given x and y data.

    Args:
    x_data (list): The x-axis data points.
    y_data (list): The y-axis data points.
    x_label (str): The label for the x-axis.
    y_label (str): The label for the y-axis.

    Returns:
    str: The HTML content of the plot.

    """
    if np.shape(x_data) != np.shape(y_data):
        raise ValueError(f"x of shape {np.shape(x_data)} and y of shape {np.shape(y_data)} are mismatched.")

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(x=x_data, y=y_data, mode="lines", hoverinfo="skip"),
    )

    fig.update_layout(
        title_x=0.5,
        showlegend=False,
        xaxis_title=x_label,
        yaxis_title=y_label,
        height=500,
        width=500,
        margin={
            "l": 50,
            "r": 10,
            "t": 10,
        }
    )

    return fig.to_html(config={"displaylogo": False}, include_mathjax="cdn", full_html=False)
