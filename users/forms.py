from django import forms


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

