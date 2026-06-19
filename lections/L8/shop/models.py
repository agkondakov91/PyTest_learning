# Create your models here.
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Категория",
    )
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Товар",)
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name

    def discounted_price(self, discount_percent: float) -> float:
        """Возвращает цену товара со скидкой."""
        if not (0 <= discount_percent <= 100):
            raise ValueError("Скидка должна быть от 0 до 100")

        return round(float(self.price) * (1 - discount_percent / 100), 2)
