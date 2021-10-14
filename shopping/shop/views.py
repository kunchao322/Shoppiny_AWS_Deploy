from django.db.models.fields import files
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Category, Product

# Create your views here.

#request function

def index(request, c_slug = None):
    c_page = None #Category
    products = None
    if c_slug != None:
        c_page  = get_object_or_404(Category, slug = c_slug)
        products = Product.objects.filter(Category=c_page,available = True)
    else:
        products = Product.objects.all().filter(available = True)
    return render(request, 'shop/category.html', {'category':c_page, 'products':products}) #pass a dictionary

#ist category view
def allProdCat(request, c_slug = None):
    c_page = None #Category
    products = None
    if c_slug != None:
        c_page  = get_object_or_404(Category, slug = c_slug)
        products = Product.objects.filter(Category=c_page,available = True)
    else:
        products = Product.objects.all().filter(available = True)
    return render(request, 'shop/category.html', {'category':c_page, 'products':products}) #pass a dictionary
 
def ProductCatDetail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category_slug = c_slug, slug = product_slug)
    except Exception as e:
        raise e
    return render(request, 'shop/product.html',{'product':product})
