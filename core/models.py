from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/')
    stock = models.PositiveIntegerField(default=1)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})
    
    def final_price(self):
        return self.discount_price or self.price
    
    def discount_percentage(self):
        if self.discount_price and self.price > 0:
            desconto = self.price - self.discount_price
            porcentagem = (desconto / self.price) * 100
            return round(porcentagem)
        return 0
    
    def __str__(self):
        return self.name
