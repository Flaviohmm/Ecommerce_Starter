from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
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
    path(
        'password_reset',
        auth_views.PasswordResetView.as_view(
            template_name='accounts/password_reset.html',
            form_class=forms.CustomPasswordResetForm,
        ),
        name='password_reset'
    ),
    path(
        'password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_confirm.html',
            form_class=forms.CustomSetPasswordForm
        ),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
        name='password_reset_complete'
    ),
]
