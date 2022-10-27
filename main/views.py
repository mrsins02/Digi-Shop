from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic.base import View, TemplateView

from main.forms import ContactUsForm
from main.models import SiteSetting


class HomeView(TemplateView):
    template_name = "main/home.html"

    def get_context_data(self, **kwargs):
        _context = super(HomeView, self).get_context_data(**kwargs)
        context = {

        }
        _context.update(context)
        return _context


class AboutUsView(TemplateView):
    template_name = "main/about.html"

    def get_context_data(self, **kwargs):
        _context = super(AboutUsView, self).get_context_data(**kwargs)
        setting = SiteSetting.objects.filter(is_active=True).first()
        context = {
            "setting": setting
        }
        _context.update(context)
        return _context


class ContactUsView(FormView):
    template_name = "main/contact.html"
    form_class = ContactUsForm
    success_url = reverse_lazy("contact")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        name_and_family = form.cleaned_data.get("name_and_family")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")
        # todo : send mail
        return super(ContactUsView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        _context = super(ContactUsView, self).get_context_data(**kwargs)
        setting = SiteSetting.objects.filter(is_active=True).first()
        context = {
            "setting": setting
        }
        _context.update(context)
        return _context


def header_component(request):
    return render(request, "includes/header-component.html")


def footer_component(request):
    return render(request, "includes/footer-component.html")
