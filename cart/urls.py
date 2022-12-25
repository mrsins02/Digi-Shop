from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import CartView, add_to_cart, delete_from_cart, clean_cart

urlpatterns = [
    path('', CartView.as_view(), name="cart"),
    path('add-to-cart/', add_to_cart, name="add_to_cart"),
    path('delete-from-cart/', delete_from_cart, name="delete_from_cart"),
    path('clean-cart/', clean_cart, name="clean_cart"),
]
