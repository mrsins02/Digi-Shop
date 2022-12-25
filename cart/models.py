from django.db import models
from django.db.models import Sum

from users.models import User
from products.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    created = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField(blank=True, default=0, verbose_name="قیمت نهایی")
    tax = models.IntegerField(blank=True, default=0, verbose_name="مالیات")
    is_paid = models.BooleanField(blank=True, default=False, verbose_name="وضعیت پرداخت")
    pay_date = models.DateTimeField(blank=True, null=True)

    def get_total_price(self):
        products = self.cartproducts_set.all().aggregate(sum=Sum("total_price"))
        return products["sum"]

    def get_final_price(self):
        return self.total_price - self.tax

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.id:
            self.total_price = self.get_total_price()
            self.tax = (self.total_price * 9) / 100
        else:
            self.total_price = 0
            self.tax = 0
        return super(Cart, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return f"{self.user.username}({self.created.date()})"

    class Meta:
        verbose_name = "سبد خرید"
        verbose_name_plural = "سبد های خرید"


class CartProducts(models.Model):
    cart_object = models.ForeignKey(Cart, on_delete=models.CASCADE, default=0, verbose_name="سبد خرید")
    product: Product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    product_final_price = models.IntegerField(blank=True, default=0, verbose_name="قیمت نهایی محصول")
    count = models.IntegerField(default=1, verbose_name="تعداد")
    total_price = models.IntegerField(default=0, verbose_name="قیمت نهایی")

    def get_total_price(self):
        if self.cart_object.is_paid:
            return self.count * self.product_final_price
        return self.count * self.product.price

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.total_price = self.get_total_price()
        return super(CartProducts, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return f"{self.product}({self.cart_object})"

    class Meta:
        verbose_name = "محصول سبد خرید"
        verbose_name_plural = "محصولات سبد خرید"
        ordering = "id",
