import pint
import plotly.graph_objs as go


def make_plot(x_data: pint.Quantity, y_data: pint.Quantity) -> str:
    """Create a plotly html representation as string.

    Args:
        x_data (pint.Quantity): x values
        y_data (pint.Quantity): y values

    Returns:
        HTML rendered graph object

    """
    if not hasattr(x_data, "__len__") or isinstance(x_data, str):
        raise TypeError("x and y must either be list or NDArray")

    if not hasattr(y_data, "__len__") or isinstance(y_data, str):
        raise TypeError("x and y must either be list or NDArray")

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(x=x_data.magnitude, y=y_data.magnitude, mode="lines", hoverinfo="skip"),
    )

    fig.update_layout(paper_bgcolor="rgba(0, 0, 0, 0)", margin={"l": 5, "r": 5, "t": 5, "b": 5}, width=400, height=400)

    return fig.to_html(config={"displaylogo": False}, include_mathjax="cdn", full_html="false")
