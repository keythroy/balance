
from django.shortcuts import render # type: ignore
from django.shortcuts import redirect # type: ignore
from budget.forms import BudgetForm
from budget.models import Budget


def dbg(msg):
    print(f':::::balance::::: {msg} ')

def budget(request):
    dbg(f'::Formulário budget enviado. Request method: {request.method}')
    
    success = False
    if request.method == 'POST':

#        form = BudgetForm(request.POST)
#        if form.is_valid():
#            success = True
#            dbg('Formulário válido')
#            new_register = form.save()
#            new_register.save()
#            response = redirect('/budget/')
#            return response
#
#        else:
#            dbg('Formulário inválido')
#            print(form.errors)
        pass
       
    else:
        form = BudgetForm()

    
    context = {
        'form': form,
        'success': success
    }
    

    return render(request, 'register/sign-up.html', {'form': form})

    
