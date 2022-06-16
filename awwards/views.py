from django.shortcuts import render,redirect
from .forms import ProjectSubmissionForm,UpdateProjectForm,RateProjectForm
from .models import Projects,Rating
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def homepage(request):
    '''
    View function that renders homepage
    '''
    projects = Projects.objects.all()

    return render(request, 'awwards/homepage.html', {"projects": projects})

@login_required()
def publish_project(request):
    '''
    View function that render postproject page
    '''
    if request.method == 'POST':
        form = ProjectSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            project= Projects()
            project.user = form.cleaned_data['user']
            project.title = form.cleaned_data['title']
            project.article = form.cleaned_data['article']
            project.link = form.cleaned_data['link']
            project.image = form.cleaned_data['image']
            project.save()
            messages.success(request, f'Your project has been submitted')
            return redirect('homepage')
    else:
        form = ProjectSubmissionForm()

    return render(request, 'awwards/submitproject.html', {"form":form})

@login_required()
def update_project(request):
    '''
    View function that render project update from
    '''
    form = UpdateProjectForm()
    return render(request, 'awwards/project.html',{"form":form})


def view_project(request, project_id):
    '''
    View function that render project on one page 
    '''
    project = Projects.objects.get(pk = project_id)
    return render(request, 'awwards/singleproject.html',{"project":project})


def rate_project(request,id):

    project = Projects.objects.get(id = id)

    user = request.user

    
    if request.method =='POST':
        print("inside post")
        form = RateProjectForm(request.POST)
        if form.is_valid():
            rate_design = form.save(commit=False)
            rate_design.user = user
            rate_design.project = project
            # get value for the content
            # form.data.field
            # get value usability
            # get value for design
            
            # calculate avarage 
            # assign the avarage value to score field
            # rate_design.score = avg


            rate_design.save()
            return redirect('homepage')
    else:
        form = RateProjectForm()
    return render(request, 'awwards/rate_project.html',{"project":project,"form":form,"id":id})


    