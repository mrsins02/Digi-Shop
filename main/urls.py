from django.urls import path

from .views import HomeView, AboutUsView, ContactUsView, newsletter

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about-us/", AboutUsView.as_view(), name="about"),
    path("contact-us/", ContactUsView.as_view(), name="contact"),
    path("newsletter/", newsletter, name="newsletter"),
]
