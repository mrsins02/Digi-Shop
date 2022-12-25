from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic.base import TemplateView

from main.forms import ContactUsForm
from products.utils import slider_set_generator
from blog.models import Category as BlogCategory
from main.models import SiteSetting, Slider, Newsletter
from products.models import Category as ShopCategory, Product


class HomeView(TemplateView):
    template_name = "main/home.html"

    def get_context_data(self, **kwargs):
        _context = super(HomeView, self).get_context_data(**kwargs)
        sliders = Slider.objects.filter(is_active=True)
        most_viewed = Product.objects.filter(is_active=True).annotate(views=Count("productview")).order_by("-views")[:8]
        most_viewed = slider_set_generator(most_viewed, 4)
        recent_products = Product.objects.filter(is_active=True).order_by("-created")[:8]
        recent_products = slider_set_generator(recent_products, 4)
        print(most_viewed)
        context = {
            "sliders": sliders,
            "most_viewed": most_viewed,
            "recent_products": recent_products,
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
    setting = SiteSetting.objects.get(is_active=True)
    return render(request, "includes/footer-component.html", {"setting": setting})
