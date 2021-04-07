from django.urls import path
from shop.views import category

urlpatterns = [
    path('hi/', category)
]