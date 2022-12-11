from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView
from django.views.generic.base import View, TemplateView
from products.models import Category as ShopCategory
from blog.models import Category as BlogCategory
from main.forms import ContactUsForm
from main.models import SiteSetting, Slider, Newsletter


class HomeView(TemplateView):
    template_name = "main/home.html"

    def get_context_data(self, **kwargs):
        sliders = Slider.objects.filter(is_active=True)
        _context = super(HomeView, self).get_context_data(**kwargs)
        context = {
            "sliders": sliders,
        }
        _context.update(context)
        return _context


class AboutUsView(TemplateView):
    template_name = "main/about.html"

    def get_context_data(self, **kwargs):
        setting = SiteSetting.objects.filter(is_active=True).first()
        _context = super(AboutUsView, self).get_context_data(**kwargs)
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
        setting = SiteSetting.objects.filter(is_active=True).first()
        _context = super(ContactUsView, self).get_context_data(**kwargs)
        context = {
            "setting": setting
        }
        _context.update(context)
        return _context


def newsletter(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if email:
            try:
                new_email = Newsletter.objects.create(email=email)
                new_email.save()
                return render(request, "main/newsletter.html", {
                    "status": 1
                })
            except:
                return render(request, "main/newsletter.html", {
                    "status": 0
                })
        return render(request, "main/newsletter.html", {
            "status": 0
        })


def header_component(request):
    shop_categories = ShopCategory.objects.filter(parent_id=None)
    blog_categories = BlogCategory.objects.filter(parent_id=None)

    return render(request, "includes/header-component.html", {
        "shop_categories": shop_categories,
        "blog_categories": blog_categories,
    })


def footer_component(request):
    return render(request, "includes/footer-component.html")
