from django.shortcuts import render, get_object_or_404
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

def product_list(request):
    # Pegar todos os produtos disponíveis
    products = Product.objects.filter(available=True).order_by('-created')

    # Filtro por categoria via GET (?category=slug)
    category_slug = request.GET.get('category')
    if category_slug:
        products = products.filter(category__slug=category_slug)

    # Categorias para menu lateral ou filtro
    categories = Category.objects.filter(parent__isnull=True)

    context = {
        'products': products,
        'categories': categories,
        'title': 'Todos os Produtos - Starter',
    }

    return render(request, 'core/product_list.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)

    # Produtos relacionados (mesma categoria, excluindo o atual)
    related_products = Product.objects.filter(
        category=product.category,
        available=True
    ).exclude(slug=slug)[:4]

    context = {
        'product': product,
        'related_products': related_products,
        'title': f"{product.name}",
    }

    return render(request, 'core/product_detail.html', context)