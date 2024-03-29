from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import (
    Car_Type_Form,
    Car_Upload_Form,
    Car_Model_Form,
    Part_Upload_Form,
    Problem_Upload
)
from .models import (
    Car_Type,
    Car_Model,
    Car,
    Part,
    Problem
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
    car_types = Car_Type.objects.all()
    # car_models = Car_Model.objects.all()
    if request.method == 'POST':
        form = Car_Type_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(car_type_upload)
    else:
        form = Car_Type_Form()
    
    context = {
        "title":"upload car type",
        "form":form,
        "car_types":car_types,
        # "car_models":car_models
    }
    return render(request,"main/car_type_upload_form.html",context)

@login_required
def car_model_addition(request):
    '''
    This view will upload the car model type
    '''
    car_models = Car_Model.objects.all()
    if request.method == 'POST':
        form = Car_Model_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(car_model_addition)
    else:
        form = Car_Model_Form()
    context = {
        "title":"upload car model",
        "form":form,
        "car_models":car_models
    }
    return render(request,"main/car_model_upload_form.html",context)

@login_required
def car_parts_upload(request):
    '''
    This view will enable upload of parts
    '''
    car_parts = Part.objects.all()
    if request.method == 'POST':
        form = Part_Upload_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(car_parts_upload)
    else:
        form = Part_Upload_Form()
    
    context = {
        "title":"car part upload",
        "form":form,
        "car_parts":car_parts
    }
    return render(request,"main/car_part_upload.html",context)

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
        form = Problem_Upload(request.user)
    
    context = {
        "title":"car problem upload",
        "form":form
    }

    return render(request,"main/car_problem_upload.html",context)

@login_required
def data_query(request):
    '''
    Will house the functionality searching for the data that one wants
    '''
    car_types = Car_Type.objects.all()

    context = {
        "title":"Data center",
        "car_types":car_types
    }
    return render(request,"main/data_query.html",context)

@login_required
def car_type_filter(request):
    '''
    Will render the page with the cartype so as to be able to search for specific model car
    '''
    if 'car' in request.GET and request.GET.get('car'):
        filterd_car = request.GET.get('car')
        car_type = Car_Type.objects.filter(car_type_name__icontains=filterd_car)
        car_models = Car_Model.objects.filter(car_type__car_type_name__icontains=filterd_car)
        car_problems = Problem.objects.filter(car__car_type__car_type_name__icontains=filterd_car)
    context = {
        "title":"car type",
        "car_type":car_type,
        "car_models":car_models,
        "car_problems":car_problems
    }
    return render(request,"main/car_type_filter.html",context)