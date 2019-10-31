from django import forms
from .models import (
    Car_Type,
    Car_Model,
    Car,
    Part,
    Problem,
)

class Car_Type_Form(forms.ModelForm):
    '''
    Form for uploading the car type from (Toyota,Subs)
    '''
    class Meta:
        model = Car_Type
        fields = ('car_type_name','description')

class Car_Model_Form(forms.ModelForm):
    '''
    Form for uploading the car model from a car type
    '''
    class Meta:
        model = Car_Model
        fields = ('car_model_image','car_model_name','verson','date_realised')

class Car_Upload_Form(forms.ModelForm):
    '''
    Form for uploading the users car
    '''
    class Meta:
        model = Car
        fields = ('car_image','registration_number','car_type','model','mileage','date_bought')

class Part_Upload_Form(forms.ModelForm):
    '''
    Form for uploading car parts
    '''
    class Meta:
        model = Part
        fields =('part_image','part_name')

class Problem_Upload(forms.ModelForm):
    '''
    Form for uploading a car problem
    '''
    part = forms.ModelChoiceField(queryset=Part.objects.all())
    class Meta:
        model = Problem
        fields = ('problem_name','problem_description','part','fix','car','notes')

    def __init__(self, user, *args, **kwargs):
        super(Problem_Upload, self).__init__(*args, **kwargs)
        self.fields['car'].queryset = Car.objects.filter(owner=user)