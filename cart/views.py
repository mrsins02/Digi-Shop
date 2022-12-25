from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from products.models import Product
from .models import Cart, CartProducts


class CartView(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart.objects.get_or_create(user=request.user, is_paid=False)[0]
        return render(request, "cart/cart.html", {
            "cart": cart
        })


@login_required()
def add_to_cart(request):
    product_id = request.GET.get("product_id")
    user = request.user
    cart = Cart.objects.get_or_create(user=user, is_paid=False)[0]
    product = Product.objects.filter(id=product_id)
    if product.exists():
        cart_product = CartProducts.objects.filter(cart_object_id=cart.id, product_id=product_id)
        if not cart_product.exists():
            new_cart_product = CartProducts.objects.create(cart_object_id=cart.id, product=product.first())
            new_cart_product.save()
            cart.save()
            return JsonResponse({"status": 200, "message": "Successfully Added."})
        else:
            cart_product = cart_product.first()
            cart_product.count += 1
            cart_product.save()
            cart.save()
            return JsonResponse({"status": 400, "message": "Product has been added!"})
    else:
        return JsonResponse({"status": 404, "message": "Product not found!"})


@login_required()
def delete_from_cart(request):
    product_id = request.GET.get("product_id")
    user = request.user
    cart = Cart.objects.get(user_id=user.id, is_paid=False)
    cart_product = CartProducts.objects.filter(product_id=product_id, cart_object_id=cart.id)
    if cart_product.exists():
        product = cart_product.first()
        product.delete()
        cart.save()
        return render(request, "cart/includes/table.html", {"cart": cart})
    else:
        html_message = render_to_string("cart/includes/table.html", {"cart": cart})
        return JsonResponse({"status": 404, "message": "محصول یافت نشد!", "html": html_message})


@login_required()
def clean_cart(request):
    user = request.user
    cart = Cart.objects.get_or_create(user_id=user.id, is_paid=False)[0]
    cart.delete()
    cart.save()
    return render(request, "cart/includes/table.html", {"cart": cart})
