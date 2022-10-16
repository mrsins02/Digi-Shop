from django.urls import path

from favorites.views import FavoritesView, add_to_favorites, delete_from_favorites, clean_favorites

urlpatterns = [
    path("", FavoritesView.as_view(), name="favorites"),
    path("add-to-favorites/", add_to_favorites, name="add_to_favorites"),
    path("delete-from-favorites/", delete_from_favorites, name="delete_from_favorites"),
    path("clean-favorites/", clean_favorites, name="clean_favorites"),
]
