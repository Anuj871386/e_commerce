from django.urls import path
from . import views


urlpatterns = [
    path("products/", views.add_product, name="add_product"),
    path("orders/", views.place_order, name="place_order"),
    path('top-products/', views.top_products, name='top_products'),
    path('revenue-per-product/', views.revenue_per_product, name='revenue_per_product'),
    path('top-products-page/', views.top_products_page, name='top_products_page'),
]