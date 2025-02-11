import numpy as np
from django.http import HttpResponse
from django.shortcuts import render

from .forms import QuantumNumberForm
from .pytools.lineplot import make_plot
from .pytools.schroedinger import Schroedinger


def ui_landing_page(request) -> HttpResponse:
    form = QuantumNumberForm()
    model = Schroedinger()
    x_data = model.x[1:-1]
    y_data = model.get_w_v()[1]

    n = 0

    # fig_infinite = make_plot(x_data, y_data[int(n)], x_label=r"x", y_label=r"$\psi$")
    # fig_infinite_sq = make_plot(x_data, np.abs(y_data[int(n)]) ** 2, x_label=r"x", y_label=r"$\left|\psi\right|^2$")

    if request.method == "GET":
        n = request.GET.get("quantum_number") or 0

        fig_infinite = make_plot(x_data, y_data[int(n)], x_label=r"x", y_label=r"$\psi$")
        fig_infinite_sq = make_plot(x_data, np.abs(y_data[int(n)]) ** 2, x_label=r"x", y_label=r"$\left|\psi\right|^2$")

    context = {
        "form": form,
        "fig_infinite": fig_infinite,
        "fig_infinite_sq": fig_infinite_sq,
    }

    return render(request, "px_quantum/index.html", context)
