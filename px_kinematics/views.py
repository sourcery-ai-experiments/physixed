from django.http import HttpRequest, HttpResponse
from django.template.response import TemplateResponse

from px_main.pytools.utils import ureg

from .forms import FreeFallForm
from .pytools.utils import FreeFallModel

ureg.default_format = "~P"


def ui_landing_page(request: HttpRequest) -> HttpResponse:
    """Create main entrypoint of the webpage.

    Args:
        request (HttpRequest): HttpRequest to the webpage. Either GET or POST.

    Returns:
        HttpResponse: Response of the entrypoint

    """
    form = FreeFallForm()
    time = 0

    if request.method == "POST":
        form = FreeFallForm(request.POST)
        if form.is_valid():
            distance = form.cleaned_data["distance"]
            velocity = form.cleaned_data["velocity"]
            free_fall_model = FreeFallModel(initial_h=(distance, "m"), initial_v=(velocity, "m/s"))
            time = free_fall_model.solve_endtime()
    context = {
        "form": form,
        "time": time,
    }

    return TemplateResponse(request, "px_kinematics/main.html", context)
