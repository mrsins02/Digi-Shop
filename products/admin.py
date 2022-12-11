from django.contrib import admin
from .models import Category, Brand, Product, ProductPicture, ProductComment


class ProductPictureInline(admin.TabularInline):
    model = ProductPicture


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductPictureInline,
    ]
    related_search_fields = {
        'brand': ('title', 'english_title'),
    }
    list_display = ("title", "brand", "price", "count", "is_active")
    list_editable = ("price", "count", "is_active")
    list_filter = ("category", "brand", "created", "modified", "is_active")


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductPicture)
admin.site.register(ProductComment)
