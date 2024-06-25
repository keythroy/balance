from django.shortcuts import render, redirect # type: ignore
from register.forms import RegisterForm, SignInForm
from register.models import Register


def dbg(msg):
    print(f':::::balance::::: {msg} ')

def register(request):
    dbg(f':: Register form. Request method: {request.method}')

    
    success = False
    if request.method == 'POST':

        form = RegisterForm(request.POST)
        message = ''
        if form.is_valid():
            success = True
            dbg('Form valid')
            new_register = form.save()
            new_register.save()
            message = 'User registered successfully'
            response = redirect('/budget/', message)
            return response

        else:
            dbg('Form invalid')
            print(form.errors)
       
    else:
        form = RegisterForm()
    
    context = {
        'form': form,
        'success': success
    }
    

    return render(request, 'register/sign-up.html', {'form': form})

    
def signin(request):
    dbg(f':: Sign-In Register form. Request method: {request.method}')

    
    success = False
    if request.method == 'POST':

        form = SignInForm(request.POST)
        message = ''
        if form.is_valid():
            success = True
            dbg('Form valid')
            ### login realizado com sucesso
            response = redirect('/budget/', message)
            return response

        else:
            dbg('Form invalid')
            print(form.errors)
       
    else:
        form = SignInForm()
    
    context = {
        'form': form,
        'success': success
    }
    

    return render(request, 'register/sign-in.html', {'form': form})



def signup(request):
    dbg(f':: Sin-Up Register form. Request method: {request.method}')

    
    success = False
    if request.method == 'POST':

        form = SignInForm(request.POST)
        message = ''
        if form.is_valid():
            success = True
            dbg('Form valid')
            response = redirect('/sining/', message)
            return response

        else:
            dbg('Form invalid')
            print(form.errors)
       
    else:
        form = SignInForm()
    
    context = {
        'form': form,
        'success': success
    }
    

    return render(request, 'register/sign-in.html', {'form': form})
