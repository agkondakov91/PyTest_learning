# Create your views here.
from django.shortcuts import get_object_or_404, render

from shop.models import Product


def product_list(request):
    """Список активных товаров."""
    products = Product.objects.filter(is_active=True)
    return render(request, "shop/product_list.html", {"products": products})


def product_detail(request, pk: int):
    """Детальная страница товара."""
    product = get_object_or_404(Product, pk=pk, is_active=True)
    return render(request, "shop/product_detail.html", {"product": product})
