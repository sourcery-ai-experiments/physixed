from django.http import HttpRequest, HttpResponse
from django.template.response import TemplateResponse

from .forms import FreeFallForm


def ui_landing_page(request: HttpRequest) -> HttpResponse:
    """Create main entrypoint of the webpage.

    Args:
        request (HttpRequest): HttpRequest to the webpage. Either GET or POST.

    Returns:
        HttpResponse: Response of the entrypoint

    """
    form = FreeFallForm()

    if request.method == "POST":
        form = FreeFallForm(request.POST)
        if form.is_valid():
            distance = form.cleaned_data["distance"]
    context = {
        "form": form,
        "distance": distance,
    }

    return TemplateResponse(request, "px_kinematics/main.html", context)
