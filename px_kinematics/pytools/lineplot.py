import plotly.graph_objs as go
from numpy._typing import NDArray


def make_plot(x_data: NDArray | list, y_data: NDArray | list) -> str:
    """Create a plotly html object.

    Args:
        x_data (NDArray|list): x values
        y_data (NDArray|list): y values

    Returns:
        Graph object

    """

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(x=x_data, y=y_data, mode="lines", hoverinfo="skip"),
    )

    return fig.to_html(config={"displaylogo": False}, include_mathjax="cdn", full_html="false")
