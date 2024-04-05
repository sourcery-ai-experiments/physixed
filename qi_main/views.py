from django.shortcuts import render


def ui_landing_page(request):
    return render(request, "qi_main/main.html", {})
