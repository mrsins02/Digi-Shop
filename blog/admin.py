from django.contrib import admin

from blog.models import Post, Category, PostComment

admin.site.register(Category)


class PostAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
            return super(PostAdmin, self).save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
admin.site.register(PostComment)
