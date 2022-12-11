import re

from django import forms
from captcha.fields import ReCaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput,
        max_length=32,
        min_length=4,
        label="نام کاربری",
    )
    password = forms.CharField(
        widget=forms.TextInput,
        max_length=32,
        # min_length=8,
        label="رمز عبور"
    )
    captcha_form = ReCaptchaField()


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput,
        max_length=32,
        min_length=4,
        label="نام کاربری",
    )
    email = forms.EmailField(
        widget=forms.EmailInput,
        label="ایمیل",
        help_text="مثال: example@example.com"
    )
    password = forms.CharField(
        widget=forms.TextInput,
        max_length=32,
        min_length=8,
        label="رمز عبور",
        help_text="رمز عبور باید ترکیبی از حروف کوچک, حروف بزرگ و اعداد باشد."
    )
    repeat_password = forms.CharField(
        widget=forms.TextInput,
        max_length=32,
        min_length=8,
        label="تکرار رمز عبور"
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        return email

    def clean_password(self):
        password = self.cleaned_data.get("password")
        have_upper = re.findall("[A-Z]", str(password))
        if not have_upper:
            raise forms.ValidationError("رمز باید ترکیبی از اعداد, حروف بزرگ و حروف کوچک باشد!")
        have_digit = re.findall("[0-9]", str(password))
        if not have_digit:
            raise forms.ValidationError("رمز باید ترکیبی از اعداد, حروف بزرگ و حروف کوچک باشد!")
        return password

    def clean_repeat_password(self):
        password = self.cleaned_data.get("password")
        repeat_password = self.cleaned_data.get("repeat_password")
        if password != repeat_password:
            raise forms.ValidationError("رمز عبور با تکرار رمز یکی نیست!")
        return repeat_password
