from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category


# Create your views here.
def index(request):
    product = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        product = Product.get_all_products_by_categoryid(categoryID)
    else:
        product = Product.get_all_products();
    data = {}
    data['product'] = product
    data['categories'] = categories
    return render(request , 'index.html', data)
