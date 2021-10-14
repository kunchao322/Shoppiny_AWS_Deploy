from django.urls import path
from . import views

app_name = 'shop'

#list for url patterns
urlpatterns = [
    path('', views.allProdCat, name = 'allProdCat'), #name for the url
    path('<slug:c_slug>/', views.allProdCat, name = 'products_by_category' ), #page based on slug
    path('<slug:c_slug>/<slug:product_slug>', views.ProductCatDetail, name = 'ProdCatDetail'),
]