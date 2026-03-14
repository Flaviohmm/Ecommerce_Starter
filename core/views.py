from django.shortcuts import render
from .models import Product, Category

def home(request):
    # Produtos em destaque: últimos 8 criados OU com desconto OU aleatórios
    featured_products = Product.objects.filter(available=True).order_by('-created')[:8]

    # Produtos com desconto (se existir)
    discounted_products = Product.objects.filter(
        available=True, discount_price__isnull=False
    ).order_by('-created')[:6]

    # Categorias principais (sem parent, ou as mais usadas)
    main_category = Category.objects.filter(parent__isnull=True)[:6]

    context = {
        'featured_products': featured_products,
        'discounted_products': discounted_products,
        'main_categories': main_category,
        'title': 'Starter - Produtos de Qualidade com Entrega Rápida',
    }
    return render(request, "core/home.html", context)