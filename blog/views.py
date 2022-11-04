from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post, Category


class PostListView(ListView):
    template_name = "blog/post-list.html"
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super(PostListView, self).get_queryset()
        if category := self.kwargs.get("category"):
            queryset.filter(category__category__title__iexact=category)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        categories = Category.objects.all()
        _context = {
            "categories": categories,
        }
        context.update(_context)
        return context


class PostDetailView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        next_obj = Post.objects.filter(id=self.object.id + 1)
        next_obj_slug = None
        if next_obj.exists():
            next_obj_slug = next_obj.first().slug
        previous_obj = Post.objects.filter(id=self.object.id - 1)
        previous_obj_slug = None
        if previous_obj.exists():
            previous_obj_slug = previous_obj.first().slug
        categories = Category.objects.all()
        _context = {
            "categories": categories,
            "next_obj_slug": next_obj_slug,
            "previous_obj_slug": previous_obj_slug,
        }
        context.update(_context)
        return context
