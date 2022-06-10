from django.shortcuts import render,redirect
from forms import *
from django.contrib import messages
#from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    '''
    Function to register new users to the database.
    '''
    if request.method == 'POST':
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"You have succesfully created an account. Proceed to Login")
            return redirect('login')
        else:
            form = UserRegisterForm()
            context = {
                'form':form
            }
            return render(request,"users/register.html",context)
                    
     