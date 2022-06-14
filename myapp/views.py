from turtle import title
from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Avg
from rest_framework import viewsets
from .serializers import *
from .models import Project
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
     

@login_required
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


@login_required    
def profile(request):
    user=request.user
    my_profile=Profile.objects.get(user=user)
    return render(request,"users/profile.html",{'my_profile':my_profile,"user":user})
       
    
@login_required
def update_profile(request):
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
    


@login_required 
def Rateproject(request,pk):
    '''
    Display a single projrct and  provide ratings for it.
    '''
    project = Project.objects.get(id=pk)
    title = 'Rating'
    project_rating = Rating.objects.filter(project=project).order_by('pk')
    current_user = request.user
    current_user_id = request.user.id
    project_rated = Rating.objects.filter(user=current_user_id)
    
    
    if request.method == 'POST':
        form = RatingUploadForm(request.POST)
        if form.is_valid():
                rate = form.save(commit=False)
                rate.user = request.user
                rate.project = project
                rate.save()
                project_ratings = Rating.objects.filter(project=project)
            
                design_mean_rating = []
                for d_rating in project_rating:
                    design_mean_rating.append(d_rating.design)
                try:
                    #design_average = sum(design_mean_rating)/len(design_mean_rating)
                    design_average = round(sum(design_mean_rating)/len(design_mean_rating),1)
                    design_percent = design_average * 10
                except ZeroDivisionError:
                    design_average = "0"
                    design_percent = 0
                
                content_mean_rating = []
                for c_rating in project_rating:
                    content_mean_rating.append(c_rating.content)
                try:
                    content_average = round(sum(content_mean_rating)/len(content_mean_rating),1)
                    content_percent = content_average * 10
                except ZeroDivisionError:
                    content_average = "0"
                    content_percent = 0
                
                usability_mean_rating = []
                for u_rating in project_rating:
                    usability_mean_rating.append(u_rating.usability)
                try:
                    usability_average = round(sum(usability_mean_rating)/len(usability_mean_rating),1)
                    usability_percent = usability_average *10
                except ZeroDivisionError:
                    usability_average = "0"
                    usability_percent = 0
                    
                    
                
            
    else:        
        form = RatingUploadForm()
        

    context = {
        "project_rating":project_rating,
        # "design_average":design_average,
        # "content_average":content_average,
        # "usability_average":usability_average,
        # "usability_percent":usability_percent,
        # "content_percent":content_percent,
        # "design_percent":design_percent,
        "project":project,
        "form":form
    }

    return render(request,"project/projectrating.html",context)

#create api
class ProjectList(viewsets.ModelViewSet):
        queryset = Project.objects.all().order_by('title')
        serializer_class =ProjectSerializer
        
class ProfileList(viewsets.ModelViewSet):
        queryset = Profile.objects.all()#.order_by('bio')
        serializer_class =ProfileSerializer