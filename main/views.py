from django.shortcuts import render
from django.views.generic.base import View, TemplateView


class HomeView(TemplateView):
    template_name = "main/home.html"

    def get_context_data(self, **kwargs):
        _context = super(HomeView, self).get_context_data(**kwargs)
        context = {

        }
        _context.update(context)
        return _context


def header_component(request):
    return render(request, "includes/header-component.html")


def footer_component(request):
    return render(request, "includes/footer-component.html")
