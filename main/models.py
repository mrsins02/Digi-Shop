import os

from django.db import models


def get_file_ext(file):
    return os.path.splitext(file)[1]


def slider_name_generator(instance, file):
    ext = get_file_ext(file)
    return f"banners/{instance.title}/{instance.title}{ext}"


class Phone(models.Model):
    phone = models.CharField(max_length=14, verbose_name="شماره تماس")

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = "شماره تماس"
        verbose_name_plural = "شماره تماس ها"


class SiteSetting(models.Model):
    title = models.CharField(max_length=72, verbose_name="عنوان")
    logo = models.ImageField(upload_to="media/site_logos/", verbose_name="لوگوی سایت")
    about_text = models.TextField()
    address = models.TextField()
    phone = models.ManyToManyField(to=Phone, verbose_name="شماره تماس(ها)")
    fax = models.CharField(max_length=72, verbose_name="فکس")
    email = models.EmailField(max_length=72, verbose_name="ایمیل")
    instagram = models.CharField(max_length=72, verbose_name="اینستاگرام")
    telegram = models.CharField(max_length=72, verbose_name="تلگرام")
    twitter = models.CharField(max_length=72, verbose_name="توییتر")
    additional_about_text = models.TextField(verbose_name="توضیحات اضافی")
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "تنظیمات"
        verbose_name_plural = "تنظیمات سایت"


class Slider(models.Model):
    title = models.CharField(max_length=128, verbose_name="عنوان")
    banner = models.ImageField(upload_to=slider_name_generator, verbose_name="بنر")
    text = models.TextField(verbose_name="متن")
    url = models.URLField(verbose_name="لینک")
    is_active = models.BooleanField(default=False, verbose_name="فعال/غیرفعال")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "بنر"
        verbose_name_plural = "بنر های سایت"
