from django import template

register = template.Library()


def currency(value):
    return f"{value:,}"


register.filter("currency", currency)
