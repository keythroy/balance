from django import forms
from budget.models import Register

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['id_budget', 'id_user', 'description',]
        widgets = {
            'id_budget': forms.TextInput(attrs={'class': 'form-control'}),
            'id_user': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'id_budget': 'Budget ID',
            'id_user': 'User ID',
            'name': 'Name',
            'description': 'Description',
        }
        error_messages = {
            'name': {
                'required': 'required',
                'max_length': 'max lenght exceeded',
            },
            'email': {
                'required': 'required',
                'invalid': 'invalid email',
            },
            'password': {
                'required': 'required',
                'max_length': 'max lenght exceeded',
            },
            'repeat_password': {
                'required': 'required',
                'max_length': 'max lenght exceeded',
            },
        }
        
