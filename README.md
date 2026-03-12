# 🛒 Django + Tailwind E-commerce Starter

Projeto base de **E-commerce desenvolvido com Django e TailwindCSS**, focado em simplicidade, organização e escalabilidade.
Este projeto pode servir como **base para lojas online, marketplaces ou micro-SaaS de vendas**.

---

# 📦 Tecnologias

* **Python**
* **Django**
* **TailwindCSS**
* **Node.js / npm**
* **HTML5**
* **SQLite (default do Django)**

Opcional para produção:

* PostgreSQL
* Redis
* Docker
* Stripe / MercadoPago

---

# 📁 Estrutura do Projeto

```
ecommerce/
│
├── ecommerce/             # Configuração principal do Django
│   ├── settings.py
│   ├── urls.py
│   └── asgi.py
│
├── theme/                 # App responsável pelo frontend
│   ├── static/
│   ├── templates/
│   │   └── base.html
│   │   
│   │
│   ├── views.py
│   ├── urls.py
│   └── apps.py
│
├── venv/                  # Ambiente virtual
│
├── manage.py
└── README.md
```

---

# 🚀 Instalação

### 1️⃣ Clonar o projeto

```bash
git clone https://github.com/Flaviohmm/Ecommerce_Starter.git
cd ecommerce
```

---

### 2️⃣ Criar ambiente virtual

Linux / Mac

```bash
python -m venv venv
source venv/bin/activate
```

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Instalar dependências

```bash
pip install django
pip install django-tailwind
```

---

### 4️⃣ Adicionar Tailwind ao Django

No **settings.py**

```python
INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "tailwind",
    "theme",
]

TAILWIND_APP_NAME = "theme"
```

---

# 🎨 Inicializar Tailwind

Criar o app frontend:

```bash
python manage.py tailwind init
```

Digite o nome:

```
theme
```

Instalar dependências:

```bash
python manage.py tailwind install
```

Rodar Tailwind em desenvolvimento:

```bash
python manage.py tailwind dev
```

---

# 🧭 Rotas

Arquivo principal:

```
ecommerce/urls.py
```

```python
from django.urls import path, include

urlpatterns = [
    path("", include("theme.urls")),
]
```

---

# 🧠 View principal

Arquivo:

```
theme/views.py
```

```python
from django.shortcuts import render

def home(request):
    return render(request, "home.html")
```

---

# 🧾 URL do App

```
theme/urls.py
```

```python
from django.urls import path
from .views import home

urlpatterns = [
    path("", home, name="home"),
]
```

---

# 🖥 Rodar o projeto

Execute as migrações:

```bash
python manage.py migrate
```

Criar admin:

```bash
python manage.py createsuperuser
```

Iniciar servidor:

```bash
python manage.py runserver
```

Abrir no navegador:

```
http://127.0.0.1:8000
```

---

# 🎨 Templates

Exemplo de estrutura:

```
theme/templates/
│
├── base.html
```

### base.html

Layout base do site.

---

# 📦 Funcionalidades planejadas

* Página inicial da loja
* Listagem de produtos
* Página de produto
* Carrinho de compras
* Checkout
* Login / Cadastro
* Painel administrativo
* Sistema de pagamentos

---

# 🔮 Melhorias futuras

* Integração com **Stripe**
* Integração com **MercadoPago**
* Sistema de cupons
* Avaliação de produtos
* API REST
* Deploy com **Docker**

---

# 📚 Referências

* Django Documentation
* TailwindCSS Documentation

---

# 👨‍💻 Autor

Projeto desenvolvido para estudos e prototipagem de aplicações **Django + Tailwind**.

---
