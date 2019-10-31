from django.shortcuts import render,redirect
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
