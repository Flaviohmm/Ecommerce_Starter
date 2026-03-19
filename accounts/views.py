from typing import Any, Dict

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import RegisterForm, AddressForm, CustomLoginForm
from core.models import Product
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse


# Carrinho em sessão
def get_cart(request: HttpRequest) -> Dict[str, Any]:
    return request.session.setdefault('cart', {})

def add_to_cart(request: HttpRequest, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_cart(request)
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session.modified = True
    messages.success(request, f"{product.name} adicionado ao carrinho!")
    return redirect('product_detail', slug=product.slug)

def cart_view(request: HttpRequest):
    cart = get_cart(request)
    products = []
    total = 0
    for pid, qty in cart.items():
        product = Product.objects.get(id=pid)
        subtotal = product.final_price() * qty
        products.append({'product': product, 'qty': qty, 'subtotal': subtotal})
        total += subtotal
    return render(request, 'accounts/cart.html', {'cart_items': products, 'total': total})

@login_required
def checkout(request: HttpRequest) -> Any:
    cart = get_cart(request)
    if not cart:
        messages.error(request, "Carrinho vazio!")
        return redirect('cart')
    
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()

            messages.success(request, "Pedido realizado com sucesso!")
            request.session['cart'] = {}
            return redirect('home')
    else:
        form = AddressForm()

    return render(request, 'accounts/checkout.html', {'form': form})

# Registro
def register(request: HttpRequest):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = CustomLoginForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        response = super().form_valid(form)

        remember_me = form.cleaned_data.get('remember')

        if remember_me:
            # Salva apenas o username em cookie (seguro, pois não é senha)
            response.set_cookie('remember_username', form.cleaned_data['username'], max_age=2592000)
        else:
            response.delete_cookie('remember_username')

        return response
