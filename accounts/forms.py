from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from .models import Address


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required = True,
        widget = forms.EmailInput(attrs={
            'class': 'block w-full px-4 py-3 pl-10 rounded-lg text-gray-600 bg-indigo-50 border border-indigo-300 focus:border-indigo-600 focus:ring-2 focus:ring-indigo-600 outline-none transition',
            'placeholder': 'seu@email.com',
        })
    )

    password1 = forms.CharField(
        label ="Senha",
        widget = forms.PasswordInput(attrs={
            'class': 'block w-full px-4 py-3 pl-10 rounded-lg text-gray-600 bg-indigo-50 border border-indigo-300 focus:border-indigo-600 focus:ring-2 focus:ring-indigo-600 outline-none transition',
            'placeholder': '••••••••',
        })
    )

    password2 = forms.CharField(
        label = "Confirmação de senha",
        widget = forms.PasswordInput(attrs={
            'class': 'block w-full px-4 py-3 pl-10 rounded-lg text-gray-600 bg-indigo-50 border border-indigo-300 focus:border-indigo-600 focus:ring-2 focus:ring-indigo-600 outline-none transition',
            'placeholder': 'Confirme sua senha',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'block w-full px-4 py-3 pl-10 rounded-lg text-gray-600 bg-indigo-50 border border-indigo-300 focus:border-indigo-600 focus:ring-2 focus:ring-indigo-600 outline-none transition',
                'placeholder': 'Digite seu usuário',
            }),
        }

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label = "Usuário",
        widget = forms.TextInput(attrs={
            'class': 'block w-full px-4 py-3 pl-10 rounded-lg text-gray-600 bg-indigo-50 border border-indigo-300 focus:border-indigo-600 focus:ring-2 focus:ring-indigo-600 outline-none transition',
            'placeholder': 'Digite seu usuário',
            'autocomplete': 'username',
            'autofocus': True,
        })
    )

    password = forms.CharField(
        label = "Senha",
        widget = forms.PasswordInput(attrs={
            'class': 'block w-full px-4 py-3 pl-10 rounded-lg text-gray-600 bg-indigo-50 border border-indigo-300 focus:border-indigo-600 focus:ring-2 focus:ring-indigo-600 outline-none transition',
            'placeholder': '••••••••',
            'autocomplete': 'current-password',
        })
    )

    remember = forms.BooleanField(
        label ="Lembrar de mim",
        required = False,
        widget = forms.CheckboxInput(attrs={
            'class': 'h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'password']

# Formulário de solicitação de reset (email)
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label = "Email cadastrado",
        max_length = 254,
        widget = forms.EmailInput(attrs={
            'class': 'block w-full pl-10 px-4 py-3 rounded-lg text-gray-600 bg-indigo-50 border border-indigo-300 focus:border-indigo-600 focus:ring-2 focus:ring-indigo-600 outline-none transition',
            'placeholder': 'seu@email.com',
            'autocomplete': 'email',
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'autofocus': True,
        })

# Formulário para definir nova senha (no link enviado por email)
class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label = "Nova senha",
        widget = forms.PasswordInput(attrs={
            'class': 'block w-full pl-10 px-4 py-3 rounded-lg text-gray-600 bg-indigo-50 border border-indigo-300 focus:border-indigo-600 focus:ring-2 focus:ring-indigo-600 outline-none transition',
            'placeholder': 'Nova senha',
            'autocomplete': 'new-password',
        })
    ) 

    new_password2 = forms.CharField(
        label = "Confirme a nova senha",
        widget = forms.PasswordInput(attrs={
            'class': 'block w-full pl-10 px-4 py-3 rounded-lg text-gray-600 bg-indigo-50 border border-indigo-300 focus:border-indigo-600 focus:ring-2 focus:ring-indigo-600 outline-none transition',
            'placeholder': 'Confirme a nova senha',
            'autocomplete': 'new-password',
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs.update({'autofocus': True})
              

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'number', 'complement', 'neighborhood', 'city', 'state', 'zip_code']
        widgets = {
            'street': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
        }
        