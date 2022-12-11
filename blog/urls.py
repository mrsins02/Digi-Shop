from django.urls import path

from blog.views import PostListView, PostDetailView,add_comment

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("categories/<slug:category>/", PostListView.as_view(), name="post_category"),
    path("authors/<slug:username>/", PostListView.as_view(), name="post_author"),
    path("posts/<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
    path('post-add-comment/', add_comment, name="post_add_comment"),
]
