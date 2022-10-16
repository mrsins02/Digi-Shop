from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView
from favorites.models import Favorite
from products.models import Product
from users.models import User


class FavoritesView(LoginRequiredMixin, ListView):
    template_name = "favorites/favorites.html"
    model = Favorite
    context_object_name = "favorites"

    def get_queryset(self):
        queryset = super(FavoritesView, self).get_queryset()
        user = User.objects.get(id=self.request.user.id)
        queryset = queryset.filter(user_id=user.id)
        return queryset


@login_required()
def add_to_favorites(request):
    product_id = request.GET.get("product_id")
    user = request.user
    product = Product.objects.filter(id=product_id)
    if product.exists():
        favorite = Favorite.objects.filter(user_id=user.id, product_id=product_id)
        if not favorite.exists():
            new_favorite = Favorite.objects.create(user_id=user.id, product=product.first())
            new_favorite.save()
            return JsonResponse({"status": 200, "message": "Successfully Added."})
        else:
            return JsonResponse({"status": 400, "message": "Product has been added!"})
    else:
        return JsonResponse({"status": 404, "message": "Product not found!"})


@login_required()
def delete_from_favorites(request):
    product_id = request.GET.get("product_id")
    user = request.user
    favorites_product = Favorite.objects.filter(user_id=user.id, product_id=product_id)
    if favorites_product.exists():
        product = favorites_product.first()
        product.delete()
        favorites = Favorite.objects.all()
        return render(request, "favorites/includes/table.html", {"favorites": favorites})
    else:
        return JsonResponse({"status": 404, "message": "Product not found!"})


@login_required()
def clean_favorites(request):
    user = request.user
    favorites = Favorite.objects.filter(user_id=user.id)
    favorites.delete()
    return render(request, "favorites/includes/table.html", {"favorites": favorites})
