import os

from django.db import models
from django.utils.text import slugify
from django_jalali.db import models as jmodels

from users.models import User


def get_file_ext(file):
    return os.path.splitext(file)[1]


def product_name_generator(instance, file):
    ext = get_file_ext(file)
    return f"products/{instance.product.slug}/{instance.product.slug}{ext}"


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


class Brand(models.Model):
    title = models.CharField(max_length=64, verbose_name="عنوان")
    english_title = models.CharField(max_length=64, verbose_name="عنوان انگلیسی")
    slug = models.SlugField(db_index=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.english_title)
        super(Brand, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "برند"
        verbose_name_plural = "برند ها"


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان", blank=True, null=True)
    english_title = models.CharField(max_length=150, verbose_name="عنوان انگلیسی")
    slug = models.SlugField(max_length=150, editable=False)
    default_picture = models.ImageField(upload_to=product_name_generator, null=True,
                                        blank=True, verbose_name="عکس پیش فرض")
    created = jmodels.jDateTimeField(auto_now_add=True)
    modified = jmodels.jDateTimeField(auto_now=True)
    category = models.ManyToManyField(to=Category, verbose_name="دسته بندی")
    brand = models.ForeignKey(to=Brand, on_delete=models.CASCADE, verbose_name="برند")
    count = models.IntegerField(verbose_name="تعداد")
    price = models.IntegerField(verbose_name="قیمت")
    about = models.TextField(verbose_name="درباره محصول", blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name="فعال/غیرفعال")

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.english_title
        self.slug = slugify(self.english_title)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"


class ProductPicture(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to=product_name_generator)
    is_default = models.BooleanField(default=False)

    class Meta:
        verbose_name = "تصویر محصول"
        verbose_name_plural = "تصاویر محصولات"
        ordering = ("-is_default",)


class ProductComment(models.Model):
    parent = models.ForeignKey("ProductComment", on_delete=models.CASCADE, blank=True, null=True, verbose_name="والد")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(verbose_name="متن نظر")

    class Meta:
        ordering = "-created",


class ProductView(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ip = models.CharField(max_length=32)
