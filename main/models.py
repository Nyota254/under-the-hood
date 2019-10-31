from django.db import models
from django.contrib.auth.models import User

class Car_Type(models.Model):
    '''
    This class will hold the diffrent types of cars their are e.g(Toyota,Subaru,Audi)
    '''
    car_type_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.car_type_name

class Car_Model(models.Model):
    '''
    This class will hold the diffrent types of models for the car their are e.g(Subaru legacy,Toyota camri,Toyota fielder)
    '''
    car_model_image = models.ImageField(upload_to='car_model_images',default='default_car_model.jpg',blank=True)
    car_model_name = models.CharField(max_length=200)
    verson = models.IntegerField()
    car_type = models.ForeignKey(Car_Type,on_delete=models.CASCADE)
    date_realised = models.DateField()

    def __str__(self):
        return f"{self.car_model_name}(Version {self.verson}) from {self.car_type.car_type_name} brand"

class Car(models.Model):
    '''
    This class will contain the specific details of a certain car
    '''
    car_image = models.ImageField(upload_to='car_images',blank=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=10)
    car_type = models.ForeignKey(Car_Type,on_delete=models.CASCADE)
    model = models.ForeignKey(Car_Model,on_delete=models.CASCADE)
    mileage = models.BigIntegerField(default=0)
    date_bought = models.DateField()
    
    def __str__(self):
        return f"{self.owner.username} Car of type {self.car_type.car_type_name}"


class Part(models.Model):
    '''
    This class will contain the parts class for diffrent parts of a car e.g(wheels,engine,body)
    '''
    part_image = models.ImageField(upload_to='part_images',default='default_car_part.jpg',blank=True)
    part_name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.part_name

class Problem(models.Model):
    '''
    This class will contain the problems that are associated with that car
    '''
    problem_name = models.CharField(max_length=40)
    problem_description = models.TextField()
    part = models.ForeignKey(Part,on_delete=models.CASCADE)
    fix = models.TextField()
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    notes = models.TextField(blank=True)
    date_entry = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.problem_name

