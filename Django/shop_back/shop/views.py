from django.http.response import JsonResponse
from shop.models import Category, Product


def category(request):
    categories = Category.objects.all()
    category_json = [category.to_JSON() for category in categories]
    return JsonResponse(category_json, safe=False)

def product(request):
    categories = Category.objects.all()
    category_json = [category.to_JSON() for category in categories]
    return JsonResponse(category_json, safe=False)