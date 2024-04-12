from django.shortcuts import render


def ui_landing_page(request):
    return render(request, "px_main/main.html", {})
