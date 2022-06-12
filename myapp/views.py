from turtle import title
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
    function to upload project for display
    '''
    current_user = request.user
    if request.method == "POST":
        form = ProjectUploadForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
            return redirect('home')
    else:
        form = ProjectUploadForm()
    context = {
        "form":form
    }

    return render(request,"project/project_upload.html",context)  
     
    
    
#@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile) 
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
    
    
#@login_required 
def Rateproject(request,pk):
    '''
    Display a single projrct and  provide ratings for it.
    '''
    project = project.objects.get(id=pk)
    title = 'Rating'
    project_rating = Rating.objects.filter(project=project).order_by('pk')
    current_user = request.user
    current_user_id = request.user.id
    project_rated = Rating.objects.filter(user=current_user_id)
    