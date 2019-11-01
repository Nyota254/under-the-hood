from django.urls import re_path
from .views import (
    index_view,
    car_type_upload,
    car_model_addition,
)

urlpatterns = [
    re_path('^$',index_view,name='index_view'),
    re_path('^UploadCarType/$',car_type_upload,name='upload-car-type'),
    re_path('^UploadCarModel/$',car_model_addition,name='upload-car-model')
]