from django.shortcuts import render # type: ignore
from register.forms import RegisterForm
from register.models import Register


def dbg(msg):
    print(f':::::balance::::: {msg} ')

def register(request):
    dbg(f'::Formulário enviado. Request method: {request.method}')
    print(f'name:   {request.POST}')
    success = False
    if request.method == 'POST':

        form = RegisterForm(request.POST)
        if form.is_valid():
            success = True
            dbg('Formulário válido')
            new_register = form.save()
            new_register.save()


        else:
            dbg('Formulário inválido')
            print(form.errors)
       
    else:
        form = RegisterForm()
    
    context = {
        'form': form,
        'success': success
    }
    

    return render(request, 'register/sign-up.html', {'form': form})
    
