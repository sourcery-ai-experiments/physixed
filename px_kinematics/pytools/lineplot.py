import plotly.graph_objs as go
from numpy import ndarray
from numpy.typing import NDArray


def make_plot(x_data: NDArray | list, y_data: NDArray | list) -> str:
    """Create a plotly html object.

    Args:
        x_data (NDArray|list): x values
        y_data (NDArray|list): y values

    Returns:
        Graph object

    """
    if not isinstance(x_data, ndarray | list) or not isinstance(y_data, ndarray | list):
        raise TypeError("x_data and y_data must be of type NDArray or list")

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(x=x_data, y=y_data, mode="lines", hoverinfo="skip"),
    )

    fig.update_layout(paper_bgcolor="rgba(0, 0, 0, 0)", margin={"l": 5, "r": 5, "t": 5, "b": 5}, width=400, height=400)

    return fig.to_html(config={"displaylogo": False}, include_mathjax="cdn", full_html="false")
