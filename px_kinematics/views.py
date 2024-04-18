from django.http import HttpRequest
from django.template.response import TemplateResponse

from .forms import FreeFallForm


def ui_landing_page(request: HttpRequest):
    form = FreeFallForm()
    distance = request.POST.get("distance") if request.method == "POST" else 0
    context = {
        "form": form,
        "distance": distance,
    }

    return TemplateResponse(request, "px_kinematics/main.html", context)
