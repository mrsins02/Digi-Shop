from django import forms


class ContactUsForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "ایمیل", "class": "form-control"}),
                             label="ایمیل")
    name_and_family = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "نام و نام خانوادگی", "class": "form-control"}),
        max_length=72, label="نام و نام خانوادگی")
    subject = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "موضوع", "class": "form-control"}),
                              max_length=72, label="موضوع")
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "متن پیام", "class": "form", "rows": "10"}),
        label="متن پیام")
