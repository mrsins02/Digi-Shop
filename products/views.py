from django.db.models import Q
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView

from .utils import slider_set_generator, get_client_ip
from .models import Product, ProductPicture, Category, Brand, ProductComment, ProductView


class ProductListView(ListView):
    template_name = "products/product-list.html"
    context_object_name = "products"
    paginate_by = 6

    def get_queryset(self):
        if category := self.kwargs.get("category"):
            queryset = Product.objects.filter(is_active=True, category__slug__exact=category).prefetch_related(
                "productpicture_set")
        elif brand := self.kwargs.get("brand"):
            queryset = Product.objects.filter(is_active=True, brand__slug__exact=brand).prefetch_related(
                "productpicture_set")
        elif search_query := self.request.GET.get("search"):
            queryset = Product.objects.filter(
                Q(title__icontains=search_query) | Q(english_title__icontains=search_query))
        else:
            queryset = Product.objects.filter(is_active=True).prefetch_related("productpicture_set")
        return queryset

    def get_context_data(self, **kwargs):
        _context = super(ProductListView, self).get_context_data()
        page_number = self.request.GET.get("page", 1)
        categories = Category.objects.all()
        brands = Brand.objects.all()
        context = {
            "page_number": int(page_number),
            "categories": categories,
            "brands": brands,
        }
        _context.update(context)
        return _context


class ProductDetailView(DetailView):
    template_name = "products/product-detail.html"
    # model = Product
    context_object_name = "product"

    def get_queryset(self):
        return Product.objects.filter(is_active=True).prefetch_related("productpicture_set")

    def get_context_data(self, **kwargs):
        _context = super(ProductDetailView, self).get_context_data()
        pictures = ProductPicture.objects.filter(product__slug=self.kwargs.get("slug"))
        pictures_set = slider_set_generator(pictures, 3)
        categories = Category.objects.all()
        brands = Brand.objects.all()
        related_products = Product.objects.filter(brand=self.object.brand).exclude(id=self.object.id).order_by(
            "-modified")[0:4]
        comments = ProductComment.objects.filter(product_id=self.object.id)
        ip = get_client_ip(self.request)
        visit = ProductView.objects.filter(product_id=self.object.id, ip=ip)
        if not visit.exists():
            new_visit = ProductView.objects.create(product_id=self.object.id, ip=ip)
            new_visit.save()
        context = {
            "pictures_set": pictures_set,
            "categories": categories,
            "brands": brands,
            "related_products": related_products,
            "comments": comments,
        }
        _context.update(context)
        return _context


def add_comment(request):
    if request.user.is_authenticated:
        parent_id = request.GET.get("parent_id")
        user_id = request.user.id
        product_id = request.GET.get("product_id")
        text = request.GET.get("text")
        product = Product.objects.filter(id=product_id)
        if product.exists():
            product = product.first()
            if text:
                if parent_id == "none":
                    new_comment = ProductComment.objects.create(parent_id=None, user_id=user_id, product_id=product_id,
                                                                text=text)
                    new_comment.save()
                    comments = ProductComment.objects.filter(product_id=product_id)
                    html_text = render_to_string("products/includes/comment-component.html", {"comments": comments})
                    return JsonResponse({"html": html_text, "status": 200, "message": "نظر با موفقیت ثبت شد."})
                else:
                    parent_comment = ProductComment.objects.filter(id=parent_id)
                    if parent_comment.exists():
                        new_comment = ProductComment.objects.create(parent_id=parent_id, user_id=user_id,
                                                                    product_id=product_id,
                                                                    text=text)
                        new_comment.save()
                        comments = ProductComment.objects.filter(product_id=product_id)
                        html_text = render_to_string("products/includes/comment-component.html", {"comments": comments})
                        return JsonResponse({"html": html_text, "status": 200, "message": "نظر با موفقیت ثبت شد."})
                    else:
                        return JsonResponse({"status": 404, "message": "نظر پیدا نشد!"})


            else:
                return JsonResponse({"status": 400, "message": "متن نظر را وارد کنید!"})
        else:
            return JsonResponse({"status": 404, "message": "محصول یافت نشد!"})
    return JsonResponse({"status": 302, "message": "شما وارد حساب خود نشده اید!"})
