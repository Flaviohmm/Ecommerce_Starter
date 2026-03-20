from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("produtos/", views.product_list, name="product_list"),
    path("produto/<slug:slug>/", views.product_detail, name="product_detail"),
    path("categorias/", views.category_list, name="category_list"),
    path("categoria/<slug:slug>/", views.category_detail, name="category_detail"),
]