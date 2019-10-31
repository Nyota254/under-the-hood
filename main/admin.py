from django.contrib import admin
from .models import (
    Car_Type,
    Car_Model,
    Car,
    Part,
    Problem
)

admin.site.register(Car_Type)
admin.site.register(Car_Model)
admin.site.register(Part)
admin.site.register(Car)
admin.site.register(Problem)
