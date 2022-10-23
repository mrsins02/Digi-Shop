from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, ProductPicture, Category, Brand
from .utils import slider_set_generator


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
            queryset = Product.objects.filter(Q(title__icontains=search_query) | Q(english_title__icontains=search_query))
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
            "-modified")[0:6]
        related_products = slider_set_generator(related_products, 3)
        context = {
            "pictures_set": pictures_set,
            "categories": categories,
            "brands": brands,
            "related_products": related_products,
        }
        _context.update(context)
        return _context
