from django.db import models

from products.models import Product
from users.models import User


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = "محصول مورد علاقه"
        verbose_name_plural = "مورد علاقه ها"
