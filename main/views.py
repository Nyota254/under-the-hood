from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import (
    Car_Type_Form,
    Car_Upload_Form,
    Car_Model_Form,
    Part_Upload_Form,
    Problem_Upload
)

def index_view(request):
    '''
    Will render the home page
    '''
    context = {
        "title":"Home"
    }
    return render(request,'main/index.html',context)

@login_required
def car_type_upload(request):
    '''
    This view function will help in uploading of a car type
    '''
    if request.method == 'POST':
        form = Car_Type_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(car_type_upload)
    else:
        form = Car_Type_Form()
    
    context = {
        "title":"upload car type",
        "form":form
    }
    return render(request,"main/car_type_upload_form.html",context)

@login_required
def car_model_addition(request):
    '''
    This view will upload the car model type
    '''
    if request.method == 'POST':
        form = Car_Model_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(car_model_addition)
    else:
        form = Car_Model_Form()
    context = {
        "title":"upload car model",
        "form":form
    }
    return render(request,"main/car_model_upload_form.html",context)

@login_required
def car_parts_upload(request):
    '''
    This view will enable upload of parts
    '''
    if request.method == 'POST':
        form = Part_Upload_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(car_parts_upload)
    else:
        form = Part_Upload_Form()
    
    context = {
        "title":"car part upload",
        "form":form
    }
    return redirect(request,"main/car_part_upload.html",context)

@login_required
def car_upload(request):
    '''
    This view will handle the specific car upload
    '''
    if request.method == 'POST':
        form = Car_Upload_Form(request.POST,request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = request.user
            car.save()
            return redirect(car_upload)
    else:
        form = Car_Upload_Form()
    
    context = {
        "title":"car upload",
        "form":form
    }
    return render(request,"main/car_upload_form.html",context)

@login_required
def car_problem_upload(request):
    '''
    This view will handle the form for uploading a car problem
    '''
    if request.method == 'POST':
        form = Problem_Upload(request.user,request.POST)
        if form.is_valid():
            form.save()
            return redirect(car_problem_upload)
    else:
        form = Problem_Upload()
    
    context = {
        "title":"car problem upload",
        "form":form
    }

    return render(request,"main/car_problem_upload.html",context)
