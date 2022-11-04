import os

from django.db import models
from django.utils.text import slugify

from users.models import User


def get_file_ext(file):
    return os.path.splitext(file)[1]


def post_name_generator(instance, file):
    ext = get_file_ext(file)
    return f"posts/{instance.slug}/{instance.slug}{ext}"


class Category(models.Model):
    title = models.CharField(max_length=64, verbose_name="عنوان")
    english_title = models.CharField(max_length=64, verbose_name="عنوان انگلیسی")
    slug = models.SlugField(db_index=True, editable=False)
    parent = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name="دسته بندی والد", null=True,
                               blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.english_title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


class Post(models.Model):
    title = models.CharField(max_length=128, verbose_name="عنوان")
    english_title = models.CharField(max_length=128, verbose_name="عنوان انگلیسی")
    slug = models.SlugField(max_length=128, editable=False)
    picture = models.ImageField(upload_to=post_name_generator, verbose_name="عکس")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, verbose_name="دسته بندی")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="نویسنده", editable=False)
    text = models.TextField(verbose_name="متن پست")
    is_active = models.BooleanField(default=True, verbose_name="فعال/غیرفعال")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.english_title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "پست"
        verbose_name_plural = "پست ها"
        ordering = ("-created",)
