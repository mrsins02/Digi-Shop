from django.http import JsonResponse
from django.template.loader import render_to_string

from blog.models import Post, Category, PostComment
from django.views.generic import ListView, DetailView


class PostListView(ListView):
    template_name = "blog/post-list.html"
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super(PostListView, self).get_queryset()
        if category := self.kwargs.get("category"):
            queryset = queryset.filter(category__category__slug__exact=category)
        if author := self.kwargs.get("username"):
            queryset = queryset.filter(author__username__exact=author)
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
        comments = PostComment.objects.filter(post_id=self.object.id)
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
            "comments": comments,
            "next_obj_slug": next_obj_slug,
            "previous_obj_slug": previous_obj_slug,
        }
        context.update(_context)
        return context


def add_comment(request):
    if request.user.is_authenticated:
        parent_id = request.GET.get("parent_id")
        user_id = request.user.id
        post_id = request.GET.get("post_id")
        text = request.GET.get("text")
        post = Post.objects.filter(id=post_id)
        if post.exists():
            if text:
                if parent_id == "none":
                    new_comment = PostComment.objects.create(parent_id=None, user_id=user_id, post_id=post_id,
                                                             text=text)
                    new_comment.save()
                    comments = PostComment.objects.filter(post_id=post_id)
                    html_text = render_to_string("blog/includes/comment-component.html", {"comments": comments})
                    return JsonResponse({"html": html_text, "status": 200, "message": "نظر با موفقیت ثبت شد."})
                else:
                    parent_comment = PostComment.objects.filter(id=parent_id)
                    if parent_comment.exists():
                        new_comment = PostComment.objects.create(parent_id=parent_id, user_id=user_id,
                                                                 post_id=post_id,
                                                                 text=text)
                        new_comment.save()
                        comments = PostComment.objects.filter(post_id=post_id)
                        html_text = render_to_string("blog/includes/comment-component.html", {"comments": comments})
                        return JsonResponse({"html": html_text, "status": 200, "message": "نظر با موفقیت ثبت شد."})
                    else:
                        return JsonResponse({"status": 404, "message": "نظر پیدا نشد!"})


            else:
                return JsonResponse({"status": 400, "message": "متن نظر را وارد کنید!"})
        else:
            return JsonResponse({"status": 404, "message": "پست یافت نشد!"})
    return JsonResponse({"status": 302, "message": "شما وارد حساب خود نشده اید!"})
