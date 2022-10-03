from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, ProductPicture, Category, Brand
from .utils import slider_set_generator


class ProductListView(ListView):
    template_name = "products/product-list.html"
    context_object_name = "products"
    paginate_by = 9

    def get_queryset(self):
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
        context = {
            "pictures_set": pictures_set
        }
        _context.update(context)
        return _context
