from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from . import forms

urlpatterns = [
    path('register/', views.register, name='register'),
    path(
        'login/',
        views.CustomLoginView.as_view(
            next_page='home',
        ), 
        name='login'
    ),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]
