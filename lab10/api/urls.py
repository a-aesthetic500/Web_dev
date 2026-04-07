from django.urls import path
from api.views import (
    ProductListAPIView,
    ProductDetailAPIView,
    CategoryListAPIView,
    CategoryDetailAPIView,
    CategoryProductsAPIView,
    # products_list, 
    # product_detail,
 )


# from api.views.mixins import (
#     ProductListAPIView,
#     ProductDetailAPIView,
# )

# from api.views.cbv import (
#     ProductListAPIView,
#     ProductDetailAPIView,
# )


# FBV
# from api.views.fbv import products_list, product_detail
 
urlpatterns = [
    
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:product_id>/', ProductDetailAPIView.as_view(), name='product-detail'),
 
    
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('categories/<int:category_id>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('categories/<int:category_id>/products/', CategoryProductsAPIView.as_view(), name='category-products'),
 
    
    #  path('products/', products_list, name='product-list'),
    #  path('products/<int:product_id>/', product_detail, name='product-detail'),
]