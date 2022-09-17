from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.views.generic.edit import FormView

from users.forms import LoginForm

user = get_user_model()


class LoginView(FormView):
    template_name = "user/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        get_user = authenticate(self.request, username=username, password=password)
        if get_user:
            login(self.request, get_user)
            return super(LoginView, self).form_valid(form)
        else:
            form.add_error(None, "نام کاربری یا رمز عبور اشتباه است!")
            return render(self.request, "user/login.html", {
                "form": form,
            })
