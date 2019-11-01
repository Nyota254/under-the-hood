from django.urls import re_path
from .views import (
    index_view,
    car_type_upload,
    car_model_addition,
    car_parts_upload,
    car_upload,
    car_problem_upload,
    data_query,
    car_type_filter,
)

urlpatterns = [
    re_path('^$',index_view,name='index_view'),
    re_path('^UploadCarType/$',car_type_upload,name='upload-car-type'),
    re_path('^UploadCarModel/$',car_model_addition,name="upload-car-model"),
    re_path('^CarPartUpload/$',car_parts_upload,name="upload-car-part"),
    re_path('^CarUpload/$',car_upload,name="car-upload"),
    re_path('^CarProplemUpload/$',car_problem_upload,name="car-problem-upload"),
    re_path('^DataQuery/$',data_query,name="data-query"),
    re_path('^filtercartype/$',car_type_filter,name="filter-car-type")
]