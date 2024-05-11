from django.http import HttpRequest, HttpResponse, JsonResponse
from django.template.response import TemplateResponse

from px_main.pytools.utils import ureg

from .forms import FreeFallForm
from .pytools.lineplot import make_plot
from .pytools.utils import FreeFallModel

ureg.default_format = "~P"


def ui_landing_page(request: HttpRequest) -> HttpResponse:
    """Create main entrypoint of the webpage.

    Args:
        request (HttpRequest): HttpRequest to the webpage. Either GET or POST.

    Returns:
        HttpResponse: Response of the entrypoint

    """
    if request.method == "POST":
        form = FreeFallForm(request.POST)
        if form.is_valid():
            distance = form.cleaned_data["distance"]
            velocity = form.cleaned_data["velocity"]
            free_fall_model = FreeFallModel(initial_h=(distance, "m"), initial_v=(velocity, "m/s"))
            results = free_fall_model.solve_eq()
            out = {
                "height": [h.magnitude for h in results["height"]],
                "time": [t.magnitude for t in results["time"]],
            }

            # Genereer de plot
            fig = make_plot(x_data=results["time"], y_data=results["height"])

            # Stuur alleen de plotgegevens naar de frontend
            plot_data = {
                "x_data": out["time"],
                "y_data": out["height"],
                "fig": fig,
            }
            return JsonResponse(plot_data)

    form = FreeFallForm()
    context = {"form": form}

    return TemplateResponse(request, "px_kinematics/index.html", context)
