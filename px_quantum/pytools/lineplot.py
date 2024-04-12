import plotly.graph_objs as go


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
    fig = go.Figure().set_subplots(1, 2)

    fig.add_trace(
        go.Scatter(x=x_data, y=y_data, mode="lines", hoverinfo="skip"),
        row=1,
        col=1,
    )

    fig.update_layout(
        title_x=0.5,
        showlegend=False,
        xaxis_title=x_label,
        yaxis_title=y_label,
        xaxis2_title=r"$x$",
        yaxis2_title=r"$\left| \psi(x) \right|^2$",
    )

    return fig.to_html(config={"displaylogo": False}, include_mathjax="cdn", full_html=False)
