from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth import get_user_model, login, authenticate

from users.models import User
from users.forms import LoginForm, RegisterForm

user = get_user_model()


class LoginView(UserPassesTestMixin, FormView):

    def test_func(self):
        if self.request.user.is_authenticated:
            return False
        else:
            return True

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

    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            return redirect(reverse("home"))
        return super(LoginView, self).dispatch(request, *args, **kwargs)


class RegisterView(UserPassesTestMixin, FormView):

    def test_func(self):
        if self.request.user.is_authenticated:
            return False
        else:
            return True

    template_name = "user/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        username = form.clean_username()
        email = form.clean_email()
        password = form.clean_password()

        # checking username
        username_check = User.objects.filter(username__exact=username)
        if username_check.exists():
            form.add_error("username", "این نام کاربری از قبل موجود است!")
            return render(self.request, "user/register.html", {
                "form": form,
            })

        # checking email
        email_check = User.objects.filter(email__exact=email)
        if email_check.exists():
            form.add_error("email", "این ایمیل از قبل موجود است!")
            return render(self.request, "user/register.html", {
                "form": form,
            })
        new_user = User.objects.create(username=username, email=email)
        new_user.set_password(password)
        new_user.save()
        # todo:send sms
        return super(RegisterView, self).form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            return redirect(reverse("home"))
        return super(RegisterView, self).dispatch(request, *args, **kwargs)
