from django.shortcuts import render,redirect
from .forms import *
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
                    

def Index_view(request):
    '''
    View for the homepage
    '''
    title = "home"
    projects = Project.objects.all().order_by('-pk')
    context = {
        "title":title,
        "projects":projects,
    }
    
    return render(request,"index.html",context)   
     

#@login_required
def Upload_Project(request):
    '''
    This is the function based view for uploading a project to the site
    '''
    current_user = request.user
    if request.method == "POST":
        form = ProjectUploadForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
            return redirect(Index_view)
    else:
        form = ProjectUploadForm()
    context = {
        "form":form
    }

    return render(request,"project/project_upload.html",context)  
     
    