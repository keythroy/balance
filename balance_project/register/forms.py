from django import forms
from register.models import Register

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['name', 'email', 'password', 'repeat_password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'repeat_password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        required = ['name', 'email', 'password', 'repeat_password']
        labels = {
            'name': 'Nome',
            'email': 'Email',
            'password': 'Senha',
            'repeat_password': 'Repita a senha',
        }
        error_messages = {
            'name': {
                'required': 'required',
                'max_length': 'Nome muito longo',
            },
            'email': {
                'required': 'required',
                'invalid': 'Email inválido',
            },
            'password': {
                'required': 'required',
                'max_length': 'Senha muito longa',
            },
            'repeat_password': {
                'required': 'required',
                'max_length': 'Senha muito longa',
            },
        }
        
class SignInForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        required = ['email', 'password']
        labels = {
            'email': 'Email',
            'password': 'Senha',
        }
        error_messages = {
            'email': {
                'required': 'required',
                'invalid': 'Email inválido',
            },
            'password': {
                'required': 'required',
                'max_length': 'Senha muito longa',
            },
            
        }
        
