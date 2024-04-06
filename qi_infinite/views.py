from django.shortcuts import render

def ui_landing_page(request):

    render(request, "qi_inifinte/main.html", {})
